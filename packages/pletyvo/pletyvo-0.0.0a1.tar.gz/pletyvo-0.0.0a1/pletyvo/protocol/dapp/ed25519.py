# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "Schema",
    "ED25519",
)

import typing

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
)

from . import abc
from .address import Address
from .auth_header import AuthHeader


class Schema:
    ED25519 = 0


class ED25519(abc.Signer):
    def __init__(self, seed: typing.Optional[bytes] = None) -> None:
        self._privatek = (
            Ed25519PrivateKey.from_private_bytes(seed)
            if seed
            else Ed25519PrivateKey.generate()
        )
        self._publik = self._privatek.public_key()

    @classmethod
    def schema(cls) -> int:
        return Schema.ED25519

    def sign(self, msg: bytes) -> bytes:
        return self._privatek.sign(msg)

    def public(self) -> bytes:
        return self._publik.public_bytes_raw()

    def address(self) -> Address:
        return Address.generate(
            sch=self.schema(),
            pub=self.public(),
        )

    def auth(self, msg: bytes) -> AuthHeader:
        return AuthHeader(
            sch=self.schema(),
            pub=self.public(),
            sig=self.sign(msg),
        )
