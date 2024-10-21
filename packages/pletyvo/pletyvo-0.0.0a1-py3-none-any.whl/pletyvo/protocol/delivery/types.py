# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "CHANNEL_CREATE_EVENT_TYPE",
    "CHANNEL_UPDATE_EVENT_TYPE",
    "MESSAGE_CREATE_EVENT_TYPE",
    "MESSAGE_UPDATE_EVENT_TYPE",
)

import typing

from pletyvo.protocol.dapp import EventType

CHANNEL_CREATE_EVENT_TYPE = EventType(0, 1, 0, 2)
CHANNEL_UPDATE_EVENT_TYPE = EventType(1, 1, 0, 2)

MESSAGE_CREATE_EVENT_TYPE = EventType(0, 2, 0, 2)
MESSAGE_UPDATE_EVENT_TYPE = EventType(1, 2, 0, 2)
