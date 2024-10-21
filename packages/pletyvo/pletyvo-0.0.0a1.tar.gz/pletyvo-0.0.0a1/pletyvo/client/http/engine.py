# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "Config",
    "HTTPDefault",
)

import typing

from aiohttp import ClientSession
import attrs

from pletyvo.types import (
    JSONType,
    JSONUnion,
)

from . import abc


_CONTENT_TYPE_KEY: typing.Final[str] = "Content-Type"
_CONTENT_TYPE_JSON: typing.Final[str] = "application/json"

_NETWORK_IDENTIFY_KEY: typing.Final[str] = "Network"


@attrs.define
class Config:
    url: str = attrs.field()

    network: typing.Optional[str] = attrs.field(default=None)


class HTTPDefault(abc.HTTPClient):
    def __init__(self, config: Config):
        self._config = config
        self._session: typing.Optional[ClientSession] = None

    @property
    def session(self) -> ClientSession:
        if self._session is None:
            self._session = ClientSession(
                base_url=self._config.url,
                raise_for_status=True,
                headers={_CONTENT_TYPE_KEY: _CONTENT_TYPE_JSON},
            )

            if (network := self._config.network) is not None:
                self._session.headers[_NETWORK_IDENTIFY_KEY] = network

        return self._session

    async def get(self, endpoint: str) -> JSONUnion:
        async with self.session.get(endpoint) as response:
            return await response.json()

    async def post(self, endpoint: str, body: JSONType) -> JSONUnion:
        async with self.session.post(endpoint, json=body) as response:
            return await response.json()
