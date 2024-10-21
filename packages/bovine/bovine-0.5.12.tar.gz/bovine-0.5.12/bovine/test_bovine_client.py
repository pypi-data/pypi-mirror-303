# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

from . import BovineClient


def test_bovine_client_host():
    actor = BovineClient(
        actor_id="https://domain.tld/users/someone", access_token="token"
    )

    assert actor.host == "domain.tld"
