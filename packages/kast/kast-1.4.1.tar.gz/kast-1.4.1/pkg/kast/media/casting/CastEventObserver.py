#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable
from typing import Any

from kast.media.casting.model.CastState import CastState
from kast.utils.log.Loggable import Loggable

Callback = Callable[[CastState], None]


class CastEventObserver(Loggable):

    def __init__(self) -> None:
        self._listeners: dict[Any, Callback] = {}

    def register(self, listener: Any, callback: Callback) -> None:
        self._listeners[listener] = callback

    def unregister(self, listener: Any) -> None:
        if listener in self._listeners.keys():
            self._listeners.pop(listener)

    def notify(self, event: CastState) -> None:
        self.log.debug(f"Cast event: '{event}'")
        for callback in self._listeners.values():
            callback(event)
