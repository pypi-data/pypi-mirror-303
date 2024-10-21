# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "EventHeader",
    "EventInput",
    "Event",
    "EventType",
    "EventBody",
    "EventResponse",
)

import typing
import base64
import json
from uuid import UUID

import attrs

from .address import Address
from .auth_header import AuthHeader
from pletyvo.types import JSONType


@attrs.define(slots=False)
class EventHeader:
    id: UUID = attrs.field()

    author: Address = attrs.field()

    @classmethod
    def from_dict(cls, d: JSONType) -> EventHeader:
        return cls(
            id=UUID(d["id"]),
            author=Address.from_str(d["author"]),
        )


@attrs.define(slots=False)
class EventInput:
    body: EventBody = attrs.field()

    auth: AuthHeader = attrs.field()

    def as_dict(self) -> JSONType:
        return {
            "body": str(self.body),
            "auth": self.auth.as_dict(),
        }


@attrs.define
class Event(EventInput, EventHeader):
    def as_dict(self) -> JSONType:
        return {
            "id": str(self.id),
            "author": str(self.author),
            "body": str(self.body),
            "auth": self.auth.as_dict(),
        }

    @classmethod
    def from_dict(cls, d: JSONType) -> Event:
        return cls(
            id=UUID(d["id"]),
            author=Address.from_str(d["author"]),
            body=EventBody(bytearray(base64.b64decode(d["body"]))),
            auth=AuthHeader(
                sch=d["auth"]["sch"],
                pub=base64.b64decode(d["auth"]["pub"]),
                sig=base64.b64decode(d["auth"]["sig"]),
            ),
        )


@attrs.define
class EventType:
    event: int = attrs.field()

    aggregate: int = attrs.field()

    version: int = attrs.field()

    protocol: int = attrs.field()

    def __repr__(self) -> str:
        return "<EventType(%r, %r, %r, %r)>" % tuple(self)

    def __bytes__(self) -> bytes:
        return bytes((self.event, self.aggregate, self.version, self.protocol))

    def __iter__(self) -> typing.Generator[int, typing.Any, None]:
        yield self.event
        yield self.aggregate
        yield self.version
        yield self.protocol


EVENT_BODY_VERSION: typing.Final[int] = 0


@attrs.define
class EventBody:
    payload: bytearray = attrs.field()

    def __repr__(self) -> str:
        return f"<EventBody(version={self.version!r}, event_type={self.event_type!r}, data={self.data!r})>"

    def __str__(self) -> str:
        return base64.b64encode(bytes(self)).decode("utf-8")

    def __bytes__(self) -> bytes:
        return bytes(self.payload)

    def __bytearray__(self) -> bytearray:
        return bytearray(self.payload)

    @property
    def version(self) -> int:
        return self.payload[0]

    @version.setter
    def version(self, version: int) -> None:
        self.payload[0] = version

    @property
    def event_type(self) -> EventType:
        return EventType(*self.payload[1:5])

    @event_type.setter
    def event_type(self, event_type: EventType) -> None:
        self.payload[1:5] = bytes(event_type)

    @property
    def data(self) -> bytes:
        return bytes(self)[5:]

    @data.setter
    def data(self, data: JSONType) -> None:
        self.payload[5:] = json.dumps(
            obj=data,
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")

    @classmethod
    def create_json(cls, data: JSONType, event_type: EventType) -> EventBody:
        body = cls(bytearray(5 + len(str(data))))

        body.version = EVENT_BODY_VERSION
        body.event_type = event_type
        body.data = data

        return body


@attrs.define
class EventResponse:
    id: UUID = attrs.field()

    def as_dict(self) -> JSONType:
        return {"id": str(self.id)}

    @classmethod
    def from_dict(cls, d: JSONType) -> EventResponse:
        return cls(id=UUID(d["id"]))
