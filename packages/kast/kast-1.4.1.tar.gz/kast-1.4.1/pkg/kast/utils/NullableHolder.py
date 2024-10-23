#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from __future__ import annotations  # TODO: Remove when support dropped for: Python < ?

from typing import Any, Generic, TypeVar, cast

T = TypeVar('T')


class NullableHolder(Generic[T]):

    def __init__(
        self,
        value: T | None = None,
        asValue: bool = False,
        defaultResult: Any | None = None
    ) -> None:
        self._value: T | None = value
        self._asValue: bool = asValue
        self._defaultResult: Any | None = defaultResult if defaultResult else self

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self._defaultResult

    def __getattribute__(self, name: str) -> Any:
        if name.startswith('_') or not self._asValue:
            return super().__getattribute__(name)

        if self._value is None:
            return self._defaultResult

        value = getattr(self._value, name)
        print(f'{name=}, {value=}')
        return getattr(self._value, name)

    @property
    def value(self) -> T | None:
        return self._value

    def isNone(self) -> bool:
        return self._value is None

    def isNotNone(self) -> bool:
        return self._value is not None

    def asValue(self, withDefaultResult: Any | None = None) -> T:
        return cast(T, NullableHolder(value=self._value, asValue=True, defaultResult=withDefaultResult))
