# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = ("AuthHeader",)

import typing
import base64

import attrs

from pletyvo.types import JSONType


@attrs.define
class AuthHeader:
    sch: int = attrs.field()

    pub: bytes = attrs.field()

    sig: bytes = attrs.field()

    def __repr__(self):
        return "<AuthHeader(sch=%r, pub=%r, sch=%r)>" % tuple(self.as_dict().values())

    def as_dict(self) -> JSONType:
        return {
            "sch": self.sch,
            "pub": base64.b64encode(self.pub).decode("utf-8"),
            "sig": base64.b64encode(self.sig).decode("utf-8"),
        }
