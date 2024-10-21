# Copyright (c) 2024 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "JSONType",
    "JSONList",
    "JSONUnion",
    "UUIDLike",
    "uuidlike_as_uuid",
)

import typing
from typing import (
    Any,
    List,
    Union,
)
from uuid import UUID


JSONType = Any
JSONList = List[JSONType]
JSONUnion = Union[JSONType, JSONList]

UUIDLike = Union[UUID, str]


def uuidlike_as_uuid(id: UUIDLike) -> UUID:
    return id if isinstance(id, UUID) else UUID(id)
