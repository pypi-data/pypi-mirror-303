#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from .SettingsObserver import SettingChangeCallback, SettingsObserver
from .SettingsRepository import SettingsRepository
from .SettingsSubscription import SettingsSubscription


class SettingsService:

    def __init__(self, repository: SettingsRepository, observer: SettingsObserver) -> None:
        self._repository: SettingsRepository = repository
        self._observer: SettingsObserver = observer

    def get(self, key: str) -> str | None:
        return self._repository.get(key=key)

    def set(self, key: str, value: str) -> None:
        currentValue = self.get(key=key)  # TODO: Create cacheing layer!
        if value != currentValue:
            self._repository.set(key=key, value=value)
            self._observer.notify(key=key, value=value)

    def subscribe(self, key: str, callback: SettingChangeCallback) -> SettingsSubscription:
        return self._observer.subscribe(key=key, callback=callback)
