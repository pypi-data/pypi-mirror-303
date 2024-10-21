# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "ChannelInput",
    "Channel",
    "ChannelCreateInput",
    "ChannelUpdateInput",
)

import typing
from uuid import UUID

import attrs

from pletyvo.protocol import dapp
from pletyvo.types import JSONType


@attrs.define
class ChannelInput:
    name: str = attrs.field(validator=attrs.validators.max_len(40))

    def as_dict(self) -> JSONType:
        return {
            "name": self.name,
        }


@attrs.define
class Channel(ChannelInput, dapp.EventHeader):
    def as_dict(self) -> JSONType:
        return {
            "id": str(self.id),
            "author": str(self.author),
            "name": str(self.name),
        }

    @classmethod
    def from_dict(cls, d: JSONType) -> Channel:
        return cls(
            id=UUID(d["id"]),
            author=dapp.Address.from_str(d["author"]),
            name=d["name"],
        )


@attrs.define
class ChannelCreateInput(ChannelInput):
    pass


@attrs.define
class ChannelUpdateInput(ChannelInput):
    pass
