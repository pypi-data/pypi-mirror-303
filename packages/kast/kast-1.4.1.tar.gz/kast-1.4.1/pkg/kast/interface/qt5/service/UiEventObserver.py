#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable
from typing import Any

from kast.interface.qt5.service.UiEvent import UiEvent
from kast.utils.log.Loggable import Loggable

Callback = Callable[[UiEvent], None]


class UiEventObserver(Loggable):

    def __init__(self) -> None:
        self._listeners: dict[Any, Callback] = {}

    def register(self, listener: Any, callback: Callback) -> None:
        self._listeners[listener] = callback

    def unregister(self, listener: Any) -> None:
        self._listeners = dict((key, value) for key, value in self._listeners.items() if key != listener)

    def notify(self, uiEvent: UiEvent) -> None:
        for callback in self._listeners.values():
            callback(uiEvent)
