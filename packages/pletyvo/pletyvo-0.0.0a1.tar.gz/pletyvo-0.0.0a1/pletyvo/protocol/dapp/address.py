# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = ("Address",)

import typing

import attrs
from blake3 import blake3


ADDRESS_SIZE: typing.Final[int] = 32
ADDRESS_LENGTH: typing.Final[int] = (ADDRESS_SIZE * 2) + 2


@attrs.define
class Address:
    data: bytes = attrs.field(
        validator=(
            attrs.validators.instance_of(bytes),
            attrs.validators.max_len(32),
            attrs.validators.min_len(32),
        )
    )

    def __repr__(self) -> str:
        return f"<{self}>"

    def __str__(self) -> str:
        return f"0x{self.data.hex()}"

    def __len__(self) -> int:
        return len(str(self))

    @classmethod
    def from_str(cls, data: str) -> Address:
        if not data.startswith("0x"):
            raise ValueError(f"Address must start with '0x', not {data[:2]!r}")

        if len(data) != ADDRESS_LENGTH:
            raise ValueError(
                f"Address must have {ADDRESS_LENGTH} characters, not {len(data)}"
            )

        return cls(bytes.fromhex(data[2:]))

    @classmethod
    def generate(cls, sch: int, pub: bytes) -> Address:
        return cls.from_str(f"0x{blake3(bytes((sch, )) + pub).hexdigest(length=32)}")
