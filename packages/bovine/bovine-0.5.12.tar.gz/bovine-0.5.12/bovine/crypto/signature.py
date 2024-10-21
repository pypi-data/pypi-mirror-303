# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

"""Helper classes to parse signatures from the HTTP Headers"""

from dataclasses import dataclass
import logging
import http_sf
from typing import List


logger = logging.getLogger(__name__)


def int_or_none(value):
    if value:
        return int(value)
    return None


@dataclass
class Signature:
    """Helper class to parse HTTP Signatures"""

    key_id: str
    """key_id"""
    algorithm: str
    """The algorithm used"""
    headers: str
    """The header fields contained in the signature"""
    signature: str
    """The signature string"""
    created: int | None = None
    """Created timestamp"""
    expires: int | None = None
    """The expires timestamp"""

    def __post_init__(self):
        if self.algorithm not in ["rsa-sha256", "hs2019"]:
            logger.error(f"Unsupported algorithm {self.algorithm}")
            logger.error(self.signature)
            logger.error(self.headers)
            logger.error(self.key_id)

            raise ValueError("Unsupported algorithm", self.algorithm)

    @property
    def fields(self) -> List[str]:
        """Returns the fields that are used when building the signature"""
        return self.headers.split(" ")

    @staticmethod
    def from_signature_header(header):
        """Takes the signature header and turns into Signature object

        The header is assumed of the for key=value,... The keys keyId,
        algorithm, headers, and signature are parsed. If algorithm
        is absent it is assumed to be rsa-sha256. The other keys are required.

        ```pycon
        >>> header = 'keyId="https://host.user#main-key",algorithm="rsa-sha256",headers="(request-target) host date digest content-type",signature="h...Kg=="'
        >>> Signature.from_signature_header(header)
        Signature(key_id='https://host.user#main-key',
            algorithm='rsa-sha256',
            headers='(request-target) host date digest content-type',
            signature='h...Kg==',
            created=None,
            expires=None)

        ```

        (created) and (expires) are supported via

        ```pycon
        >>> header = 'keyId="https://key.example",algorithm="hs2019",headers="host date (request-target) (created) (expires)",signature="s0...",created="1728671105",expires="1728674705"'
        >>> Signature.from_signature_header(header)
        Signature(key_id='https://key.example',
            algorithm='hs2019',
            headers='host date (request-target) (created) (expires)',
            signature='s0...',
            created=1728671105,
            expires=1728674705)

        ```
        """
        headers = header.split(",")
        headers = [x.split('="', 1) for x in headers]
        parsed = {x[0]: x[1].replace('"', "") for x in headers}

        created = int_or_none(parsed.get("created", None))
        expires = int_or_none(parsed.get("expires", None))
        return Signature(
            parsed["keyId"],
            parsed.get("algorithm", "rsa-sha256"),
            parsed["headers"],
            parsed["signature"],
            created=created,
            expires=expires,
        )


@dataclass
class RFC9421Signature:
    """Helper class to parse signatures according to
    [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421.html).

    Currently, RFC9421 support is in development in bovine"""

    fields: List[str]
    """fields used in the signature"""
    signature: bytes
    """The signature"""
    signature_params: str
    """The signature parameters as a string"""
    params: dict
    """The signature parameters as a dictionary"""

    @property
    def key_id(self):
        """
        Returns the id of the public key

        ```pycon
        >>> signature = RFC9421Signature(fields=[],
        ...     signature=b"",
        ...     params={"keyid": "http://actor.example/key"},
        ...     signature_params=b"")
        >>> signature.key_id
        'http://actor.example/key'

        ```
        """

        return self.params["keyid"]

    @staticmethod
    def from_headers(signature_input, signature):
        """
        ```pycon
        >>> signature_input='sig-b26=("date" "@method" "@path" "@authority" "content-type" "content-length");created=1618884473;keyid="test-key-ed25519"'
        >>> signature='sig-b26=:wqcAqbmYJ2ji2glfAMaRy4gruYYnx2nEFN2HN6jrnDnQCK1u02Gb04v9EDgwUPiu4A0w6vuQv5lIp5WPpBKRCw==:'
        >>> RFC9421Signature.from_headers(signature_input, signature)
        RFC9421Signature(fields=['date', '@method', '@path', '@authority', 'content-type', 'content-length'],
            signature=b"...",
            signature_params='("date" "@method" "@path" "@authority" "content-type" "content-length");created=1618884473;keyid="test-key-ed25519"',
            params={'created': 1618884473, 'keyid': 'test-key-ed25519'})

        ```
        """

        parsed_input = http_sf.parse_dictionary(signature_input.encode())[1]
        parsed_signature = http_sf.parse_dictionary(signature.encode())[1]

        if len(parsed_input) != 1:
            raise ValueError("Currently only one signature is supported")

        signature_key = list(parsed_input.keys())[0]
        parsed_input = parsed_input[signature_key]
        parsed_signature = parsed_signature[signature_key]

        fields = [x[0] for x in parsed_input[0]]

        return RFC9421Signature(
            fields=fields,
            signature=parsed_signature[0],
            params=parsed_input[1],
            signature_params=signature_input.split("=", 1)[1],
        )
