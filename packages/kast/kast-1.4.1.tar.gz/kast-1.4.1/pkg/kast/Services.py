#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import kast
from kast.core.AppInfo import AppInfo
from kast.core.AppRuntimeFlags import AppRuntimeFlags
from kast.core.settings.SettingsFacade import SettingsFacade
from kast.core.settings.SettingsObserver import SettingsObserver
from kast.core.settings.SettingsRepository import SettingsRepository
from kast.core.settings.SettingsService import SettingsService
from kast.core.storage.PersistentStorage import PersistentStorage
from kast.core.storage.TemporaryStorage import TemporaryStorage
from kast.media.casting.CastController import CastController
from kast.media.casting.CastEventObserver import CastEventObserver
from kast.media.processing.MediaProcessingService import MediaProcessingService
from kast.media.streaming.MediaServer import MediaServer
from kast.utils.ResourceProvider import ResourceProvider
from kast.utils.SingletonApplication import SingletonApplication


class Services:

    def __init__(self, appRuntimeFlags: AppRuntimeFlags) -> None:
        self._appLock = SingletonApplication(appName=kast.__package__)
        self.resourceProvider = ResourceProvider(kast)

        self.appRuntimeFlags: AppRuntimeFlags = appRuntimeFlags
        self.appInfo: AppInfo = AppInfo(resourceProvider=self.resourceProvider)
        self.persistentStorage: PersistentStorage = PersistentStorage(appInfo=self.appInfo)

        self._settingsRepository: SettingsRepository = SettingsRepository(dbPath=self.persistentStorage.path / 'settings.db')
        self._settingsObserver: SettingsObserver = SettingsObserver()
        self._settingsService: SettingsService = SettingsService(repository=self._settingsRepository, observer=self._settingsObserver)
        self.settingsFacade: SettingsFacade = SettingsFacade(settingsService=self._settingsService)

        self.temporaryStorage: TemporaryStorage = TemporaryStorage(appInfo=self.appInfo, settingsFacade=self.settingsFacade)

        self.castEventObserver: CastEventObserver = CastEventObserver()
        self.castController: CastController = CastController(appInfo=self.appInfo, castEventObserver=self.castEventObserver)

        self.mediaServer: MediaServer = MediaServer()

        self.mediaProcessingService = MediaProcessingService(storageDir=self.temporaryStorage.path)
