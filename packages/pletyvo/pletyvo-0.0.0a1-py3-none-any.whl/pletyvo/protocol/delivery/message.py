# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "MessageInput",
    "Message",
    "MessageCreateInput",
    "MessageUpdateInput",
)

import typing
from uuid import UUID

import attrs

from pletyvo.protocol import dapp
from pletyvo.types import (
    UUIDLike,
    uuidlike_as_uuid,
    JSONType,
)


@attrs.define
class MessageInput:
    channel: UUIDLike = attrs.field()

    content: str = attrs.field(validator=attrs.validators.max_len(2048))

    def __attrs_post_init__(self):
        self.channel = uuidlike_as_uuid(self.channel)

    def as_dict(self) -> JSONType:
        return {
            "channel": str(self.channel),
            "content": str(self.content),
        }


@attrs.define
class Message(MessageInput, dapp.EventHeader):
    def as_dict(self) -> JSONType:
        return {
            "id": str(self.id),
            "channel": str(self.channel),
            "author": str(self.author),
            "content": str(self.content),
        }

    @classmethod
    def from_dict(cls, d: JSONType) -> Message:
        return cls(
            id=UUID(d["id"]),
            channel=UUID(d["channel"]),
            author=dapp.Address.from_str(d["author"]),
            content=d["content"],
        )


@attrs.define
class MessageCreateInput(MessageInput):
    pass


@attrs.define
class MessageUpdateInput(MessageInput):
    message: UUIDLike = attrs.field()

    def __attrs_post_init__(self):
        self.message = uuidlike_as_uuid(self.message)

    def as_dict(self) -> JSONType:
        return {
            **super().as_dict(),
            "message": str(self.message),
        }
