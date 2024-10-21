# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = ("NetworkService",)

import typing
from abc import (
    ABC,
    abstractmethod,
)

from pletyvo.protocol import dapp

from .network import (
    Network,
    NetworkCreateInput,
    NetworkUpdateInput,
)


class NetworkService(ABC):
    @abstractmethod
    async def get(self) -> Network: ...

    @abstractmethod
    async def create(self, input: NetworkCreateInput) -> dapp.EventResponse: ...

    @abstractmethod
    async def update(self, input: NetworkUpdateInput) -> dapp.EventResponse: ...
