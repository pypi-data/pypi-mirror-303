# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = ("Service",)

import typing

from . import abc
from .dapp import DappService
from .registry import RegistryService
from .delivery import DeliveryService
from pletyvo.protocol.dapp import abc as _dapp_abc


class Service:
    __slots__: typing.Sequence[str] = (
        "dapp",
        "delivery",
        "registry",
    )

    def __init__(self, engine: abc.HTTPClient, signer: _dapp_abc.Signer) -> None:
        self.dapp = DappService(engine)
        self.registry = RegistryService(engine, signer, self.dapp.event)
        self.delivery = DeliveryService(engine, signer, self.dapp.event)
