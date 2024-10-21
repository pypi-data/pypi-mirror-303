# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "ChannelService",
    "MessageService",
)

import typing
from abc import (
    ABC,
    abstractmethod,
)

from pletyvo.types import (
    QueryOption,
    UUIDLike,
)
from pletyvo.protocol import dapp
from .channel import (
    Channel,
    ChannelCreateInput,
    ChannelUpdateInput,
)
from .message import (
    Message,
    MessageCreateInput,
    MessageUpdateInput,
)


class ChannelService(ABC):
    @abstractmethod
    async def get_by_id(self, id: UUIDLike) -> Channel: ...

    @abstractmethod
    async def create(self, input: ChannelCreateInput) -> dapp.EventResponse: ...

    @abstractmethod
    async def update(self, input: ChannelUpdateInput) -> dapp.EventResponse: ...


class MessageService(ABC):
    @abstractmethod
    async def get(
        self, channel: UUIDLike, option: typing.Optional[QueryOption] = None
    ) -> typing.List[Message]: ...

    @abstractmethod
    async def get_by_id(
        self, channel: UUIDLike, id: UUIDLike
    ) -> typing.Optional[Message]: ...

    @abstractmethod
    async def create(self, input: MessageCreateInput) -> dapp.EventResponse: ...

    @abstractmethod
    async def update(self, input: MessageUpdateInput) -> dapp.EventResponse: ...
