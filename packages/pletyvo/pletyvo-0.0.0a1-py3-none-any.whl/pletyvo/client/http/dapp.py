# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "EventService",
    "DappService",
)

import typing
from uuid import UUID

from . import abc
from pletyvo.protocol import dapp
from pletyvo.types import (
    QueryOption,
    uuidlike_as_uuid,
    JSONType,
    JSONList,
)


class EventService(dapp.abc.EventService):
    def __init__(self, engine: abc.HTTPClient) -> None:
        self._engine = engine

    async def get(
        self, option: typing.Optional[QueryOption] = None
    ) -> typing.List[dapp.Event]:
        response: JSONList = await self._engine.get(
            f"/api/dapp/v1/events{option or ''}"
        )
        return [dapp.Event.from_dict(d=event) for event in response]  # type: ignore

    async def get_by_id(self, id: typing.Union[UUID, str]) -> dapp.Event:
        response: JSONType = await self._engine.get(
            f"/api/dapp/v1/events/{uuidlike_as_uuid(id)}"
        )
        return dapp.Event.from_dict(response)

    async def create(self, input: dapp.EventInput) -> dapp.EventResponse:
        response: JSONType = await self._engine.post(
            "/api/dapp/v1/events", body=input.as_dict()
        )
        return dapp.EventResponse.from_dict(response)


class DappService:
    __slots__ = ("event",)

    def __init__(self, engine: abc.HTTPClient):
        self.event = EventService(engine)
