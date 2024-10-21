# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "Signer",
    "EventService",
)

import typing
from abc import (
    ABC,
    abstractmethod,
)

from .auth_header import AuthHeader
from .address import Address
from .event import (
    Event,
    EventInput,
    EventResponse,
)
from pletyvo.types import (
    UUIDLike,
    QueryOption,
)


class Signer(ABC):
    @classmethod
    @abstractmethod
    def schema(cls) -> int: ...

    @abstractmethod
    def sign(self, msg: bytes) -> bytes: ...

    @abstractmethod
    def public(self) -> bytes: ...

    @abstractmethod
    def address(self) -> Address: ...

    @abstractmethod
    def auth(self, msg: bytes) -> AuthHeader: ...


class EventService(ABC):
    @abstractmethod
    async def get(
        self, option: typing.Optional[QueryOption] = None
    ) -> typing.List[Event]: ...

    @abstractmethod
    async def get_by_id(self, id: UUIDLike) -> typing.Optional[Event]: ...

    @abstractmethod
    async def create(self, input: EventInput) -> EventResponse: ...
