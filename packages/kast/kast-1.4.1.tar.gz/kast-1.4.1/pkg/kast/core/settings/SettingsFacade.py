#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.core.settings.SettingsKeys import SettingsKeys
from kast.core.settings.SettingsObserver import SettingChangeCallback
from kast.core.settings.SettingsService import SettingsService
from kast.core.settings.SettingsSubscription import SettingsSubscription


class SettingsFacade:

    def __init__(self, settingsService: SettingsService) -> None:
        self._settingsService: SettingsService = settingsService

    def get(self, key: SettingsKeys) -> str | None:
        value = self._settingsService.get(key=key.value.key)
        return value if value is not None \
            else key.value.defaultValueFactory()

    def set(self, key: SettingsKeys, value: str) -> None:
        self._settingsService.set(key=key.value.key, value=value)

    def subscribe(self, key: SettingsKeys, callback: SettingChangeCallback) -> SettingsSubscription:
        return self._settingsService.subscribe(key=key.value.key, callback=callback)
