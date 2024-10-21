# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "ChannelService",
    "MessageService",
    "DeliveryService",
)

import typing

from . import abc
from pletyvo.types import (
    QueryOption,
    uuidlike_as_uuid,
    JSONList,
    JSONType,
    UUIDLike,
)
from pletyvo.protocol import (
    dapp,
    delivery,
)


class ChannelService(delivery.abc.ChannelService):
    def __init__(
        self,
        engine: abc.HTTPClient,
        signer: dapp.abc.Signer,
        event_service: dapp.abc.EventService,
    ) -> None:
        self._engine = engine
        self._signer = signer
        self._event_service = event_service

    async def get_by_id(self, id: UUIDLike) -> delivery.Channel:
        response: JSONType = await self._engine.get(
            f"/api/delivery/v1/channels/{uuidlike_as_uuid(id)}"
        )
        return delivery.Channel.from_dict(response)

    async def create(self, input: delivery.ChannelCreateInput) -> dapp.EventResponse:
        body = dapp.EventBody.create_json(
            data=input.as_dict(), event_type=delivery.CHANNEL_CREATE_EVENT_TYPE
        )
        return await self._event_service.create(
            input=dapp.EventInput(
                body=body,
                auth=self._signer.auth(bytes(body)),
            )
        )

    async def update(self, input: delivery.ChannelUpdateInput) -> dapp.EventResponse:
        body = dapp.EventBody.create_json(
            data=input.as_dict(), event_type=delivery.CHANNEL_UPDATE_EVENT_TYPE
        )
        return await self._event_service.create(
            input=dapp.EventInput(
                body=body,
                auth=self._signer.auth(bytes(body)),
            )
        )


class MessageService(delivery.abc.MessageService):
    def __init__(
        self,
        engine: abc.HTTPClient,
        signer: dapp.abc.Signer,
        event_service: dapp.abc.EventService,
    ) -> None:
        self._engine = engine
        self._signer = signer
        self._event_service = event_service

    async def get(
        self, channel: UUIDLike, option: typing.Optional[QueryOption] = None
    ) -> typing.List[delivery.Message]:
        response: JSONList = await self._engine.get(
            f"/api/delivery/v1/channels/{channel}/messages" + str(option or "")
        )
        return [delivery.Message.from_dict(message) for message in response]

    async def get_by_id(
        self, channel: UUIDLike, id: UUIDLike
    ) -> delivery.Message | None:
        response: JSONType = await self._engine.get(
            f"/api/delivery/v1/channels/{uuidlike_as_uuid(channel)}/messages/{uuidlike_as_uuid(id)}"
        )
        return delivery.Message.from_dict(response)

    async def create(self, input: delivery.MessageCreateInput) -> dapp.EventResponse:
        body = dapp.EventBody.create_json(
            data=input.as_dict(),
            event_type=delivery.MESSAGE_CREATE_EVENT_TYPE,
        )
        return await self._event_service.create(
            input=dapp.EventInput(
                body=body,
                auth=self._signer.auth(bytes(body)),
            )
        )

    async def update(self, input: delivery.MessageUpdateInput) -> dapp.EventResponse:
        body = dapp.EventBody.create_json(
            data=input.as_dict(),
            event_type=delivery.MESSAGE_UPDATE_EVENT_TYPE,
        )
        return await self._event_service.create(
            input=dapp.EventInput(
                body=body,
                auth=self._signer.auth(bytes(body)),
            )
        )


class DeliveryService:
    __slots__ = (
        "channel",
        "message",
    )

    def __init__(
        self,
        engine: abc.HTTPClient,
        signer: dapp.abc.Signer,
        event_service: dapp.abc.EventService,
    ):
        self.channel = ChannelService(engine, signer, event_service)
        self.message = MessageService(engine, signer, event_service)
