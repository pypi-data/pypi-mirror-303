# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "NetworkService",
    "RegistryService",
)

import typing

from . import abc
from pletyvo.protocol import (
    dapp,
    registry,
)
from pletyvo.types import JSONType


class NetworkService(registry.abc.NetworkService):
    def __init__(
        self,
        engine: abc.HTTPClient,
        signer: dapp.abc.Signer,
        event_service: dapp.abc.EventService,
    ) -> None:
        self._engine = engine
        self._signer = signer
        self._event_service = event_service

    async def get(self) -> registry.Network:
        response: JSONType = await self._engine.get("/api/registry/v1/network")
        return registry.Network.from_dict(response)

    async def create(self, input: registry.NetworkCreateInput) -> dapp.EventResponse:
        body = dapp.EventBody.create_json(
            data=input.as_dict(),
            event_type=registry.types.NETWORK_CREATE_EVENT_TYPE,
        )
        return await self._event_service.create(
            input=dapp.EventInput(
                body=body,
                auth=self._signer.auth(bytes(body)),
            )
        )

    async def update(self, input: registry.NetworkUpdateInput) -> dapp.EventResponse:
        body = dapp.EventBody.create_json(
            data=input.as_dict(),
            event_type=registry.types.NETWORK_UPDATE_EVENT_TYPE,
        )
        return await self._event_service.create(
            input=dapp.EventInput(body=body, auth=self._signer.auth(bytes(body)))
        )


class RegistryService:
    __slots__ = ("network",)

    def __init__(
        self,
        engine: abc.HTTPClient,
        signer: dapp.abc.Signer,
        event_service: dapp.abc.EventService,
    ):
        self.network = NetworkService(engine, signer, event_service)
