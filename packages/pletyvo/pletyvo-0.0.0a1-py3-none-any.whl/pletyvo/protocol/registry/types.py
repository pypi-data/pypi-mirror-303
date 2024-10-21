# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "NETWORK_CREATE_EVENT_TYPE",
    "NETWORK_UPDATE_EVENT_TYPE",
)

import typing

from pletyvo.protocol.dapp import EventType

NETWORK_CREATE_EVENT_TYPE = EventType(0, 1, 0, 1)
NETWORK_UPDATE_EVENT_TYPE = EventType(1, 1, 0, 1)
