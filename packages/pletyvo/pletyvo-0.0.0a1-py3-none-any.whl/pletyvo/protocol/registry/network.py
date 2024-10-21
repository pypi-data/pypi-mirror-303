# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "NetworkInput",
    "Network",
    "NetworkCreateInput",
    "NetworkUpdateInput",
)

import typing
from uuid import UUID

import attrs

from pletyvo.protocol import dapp
from pletyvo.types import JSONType


@attrs.define
class NetworkInput:
    name: str = attrs.field(validator=attrs.validators.max_len(40))

    def as_dict(self) -> JSONType:
        return {
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, d: JSONType) -> NetworkInput:
        return cls(name=d["name"])


@attrs.define
class Network(NetworkInput, dapp.EventHeader):
    @classmethod
    def from_dict(cls, d: JSONType) -> Network:
        return cls(
            id=UUID(d["id"]),
            name=d["name"],
            author=dapp.Address.from_str(d["author"]),
        )


@attrs.define
class NetworkCreateInput(NetworkInput):
    pass


@attrs.define
class NetworkUpdateInput(NetworkInput):
    pass
