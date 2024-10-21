# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations


__all__: typing.Sequence[str] = ("QueryOption",)

import typing
from uuid import UUID

import attrs

from ._types import (
    UUIDLike,
    uuidlike_as_uuid,
)


_NIL_UUID = UUID("00000000-0000-0000-0000-000000000000")


@attrs.define
class QueryOption:
    limit: int = attrs.field(default=0)

    order: bool = attrs.field(default=False)

    after: UUIDLike = attrs.field(default=_NIL_UUID)

    before: UUIDLike = attrs.field(default=_NIL_UUID)

    def __attrs_post_init__(self):
        self.before = uuidlike_as_uuid(self.before)
        self.after = uuidlike_as_uuid(self.after)

    def __str__(self) -> str:
        buf: typing.List[str] = []

        if self.limit != 0:
            buf.append(f"limit={self.limit}")

        if self.order:
            buf.append("order=asc")

        if self.after.version is not None:  # type: ignore
            buf.append(f"after={self.after}")

        if self.before.version is not None:  # type: ignore
            buf.append(f"before={self.before}")

        return "?" + "&".join(buf) if buf else ""
