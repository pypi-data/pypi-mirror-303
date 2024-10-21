# SPDX-FileCopyrightText: 2024 Helge
#
# SPDX-License-Identifier: MIT

from dataclasses import dataclass, field
from typing import List


@dataclass
class Multikey:
    """Represents a Multikey"""

    id: str
    controller: str
    multibase: str
    type: str = "Multikey"

    def build(self, include_context=True):
        result = {
            "id": self.id,
            "type": self.type,
            "controller": self.controller,
            "publicKeyMultibase": self.multibase,
        }
        if include_context:
            result["@context"] = "https://w3id.org/security/multikey/v1"
        return result

    @staticmethod
    def from_multibase_and_controller(controller, multibase):
        return Multikey(
            id=f"{controller}#{multibase}", controller=controller, multibase=multibase
        )


@dataclass
class Controller:
    """Experimental class to represent a controller document
    see [FEP-521a](https://codeberg.org/fediverse/fep/src/branch/main/fep/521a/fep-521a.md).

    See also the recent W3C Draft: [Controller Documents](https://www.w3.org/TR/controller-document/)

    ```pycon
    >>> multikey = Multikey(
    ... id="https://server.example/users/alice#ed25519-key",
    ... controller="https://server.example/users/alice",
    ... multibase="z6MkrJVnaZkeFzdQyMZu1cgjg7k1pZZ6pvBQ7XJPt4swbTQ2")
    >>> Controller(assertion_method=[multikey]).build()
    {'@context': ['https://www.w3.org/ns/did/v1',
        'https://w3id.org/security/multikey/v1'],
        'assertionMethod':
            [{'id': 'https://server.example/users/alice#ed25519-key',
            'type': 'Multikey',
            'controller': 'https://server.example/users/alice',
            'publicKeyMultibase': 'z6MkrJVnaZkeFzdQyMZu1cgjg7k1pZZ6pvBQ7XJPt4swbTQ2'}]}

    ```
    """

    assertion_method: List[Multikey] = field(default_factory=list)
    authentication: List[Multikey] = field(default_factory=list)

    def build(self):
        """Creates the controller document. Currently only assertion_method is supported"""
        if len(self.assertion_method) == 0:
            return {}

        return {
            "@context": [
                "https://www.w3.org/ns/did/v1",
                "https://w3id.org/security/multikey/v1",
            ],
            "assertionMethod": [
                key.build(include_context=False) for key in self.assertion_method
            ],
        }
