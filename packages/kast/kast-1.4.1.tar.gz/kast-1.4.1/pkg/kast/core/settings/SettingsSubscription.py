#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable

NotifyCallback = Callable[[str], None]
UnsubscribeCallback = Callable[[str, NotifyCallback], None]


class SettingsSubscription:

    def __init__(
        self,
        key: str,
        notifyCallback: NotifyCallback,
        unsubscribeCallback: UnsubscribeCallback
    ) -> None:
        self._key = key
        self._notifyCallback = notifyCallback
        self._unsubscribeCallback = unsubscribeCallback

    def unsubscribe(self) -> None:
        self._unsubscribeCallback(self._key, self._notifyCallback)
