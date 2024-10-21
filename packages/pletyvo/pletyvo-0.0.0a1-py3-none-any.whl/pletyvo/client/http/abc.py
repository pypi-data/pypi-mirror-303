# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = ("HTTPClient",)

import typing
from abc import (
    ABC,
    abstractmethod,
)

from pletyvo.types import JSONType, JSONUnion


class HTTPClient(ABC):
    @abstractmethod
    async def get(self, endpoint: str) -> JSONUnion: ...

    @abstractmethod
    async def post(self, endpoint: str, body: JSONType) -> JSONUnion: ...
