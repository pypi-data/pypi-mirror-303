#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from __future__ import annotations  # TODO: Remove when support dropped for: Python < ?

from typing import Any, Generic, TypeVar

from kast.utils.functional import Consumer, Mapper, Predicate, Runnable, Supplier

T = TypeVar('T')
R = TypeVar('R')


class FakePropertyAssigner:
    def __getattr__(self, name: str) -> FakePropertyAssigner:
        return self

    def __set__(self, instance: Any, value: Any) -> None:
        pass


class Maybe(Generic[T]):

    def __init__(self, value: T | None = None) -> None:
        self._value: T | None = value

    @property
    def value(self) -> T | None:
        return self._value

    def asPropertyAssigner(self) -> T | FakePropertyAssigner:
        return self._value if self._value is not None\
            else FakePropertyAssigner()

    def isEmpty(self) -> bool:
        return self._value is None

    def isPresent(self) -> bool:
        return not self.isEmpty()

    def ifEmpty(self, runnable: Runnable) -> None:
        if self.isEmpty():
            runnable()

    def ifPresent(self, consumer: Consumer[T]) -> None:
        if self._value is not None:
            consumer(self._value)

    def ifPresentOrEmpty(self, onPresent: Consumer[T], onEmpty: Runnable) -> None:
        if self._value is not None:
            onPresent(self._value)
        else:
            onEmpty()

    def orMaybe(self, other: Maybe[T]) -> Maybe[T]:
        return self if self._value is not None else other

    def orElse(self, default: T) -> T:
        return self._value if self._value is not None else default

    def orElseGet(self, supplier: Supplier[T]) -> T:
        return self._value if self._value is not None else supplier()

    def orThrow(self, supplier: Supplier[Exception]) -> T:
        if self._value is None:
            raise supplier()
        return self._value

    def map(self, mapper: Mapper[T, R | None]) -> Maybe[R]:
        newValue = None if self._value is None\
            else mapper(self._value)
        return Maybe[R](newValue)

    def flatMap(self, mapper: Mapper[T, Maybe[R]]) -> Maybe[R]:
        return Maybe[R](None) if self._value is None\
            else mapper(self._value)

    def filter(self, predicate: Predicate[T]) -> Maybe[T]:
        return self if (
                self._value is None
                or predicate(self._value)
            )\
            else Maybe[T]()
