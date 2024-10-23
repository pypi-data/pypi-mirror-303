#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import shutil
import tempfile
from pathlib import Path

from kast.core.AppInfo import AppInfo
from kast.core.settings.SettingsFacade import SettingsFacade
from kast.core.settings.SettingsKeys import SettingsKeys
from kast.utils.log.Loggable import Loggable


class TemporaryStorage(Loggable):

    def __init__(
        self,
        appInfo: AppInfo,
        settingsFacade: SettingsFacade
    ) -> None:
        self._settingsFacade: SettingsFacade = settingsFacade

        self._temporaryStorage = tempfile.TemporaryDirectory(prefix=f'{appInfo.package}-')

    @property
    def path(self) -> Path:
        return Path(self._temporaryStorage.name)

    def cleanupArtifacts(self) -> None:
        previousTemporaryPath = self._settingsFacade.get(SettingsKeys.PreviousTemporaryPath)
        if previousTemporaryPath and Path(previousTemporaryPath).exists():
            self.log.info(f"Previous session artifacts cleanup at path: '{previousTemporaryPath}'")
            try:
                shutil.rmtree(previousTemporaryPath)
            except Exception:
                self.log.error('Cleanup failed!')
                raise

        self._settingsFacade.set(SettingsKeys.PreviousTemporaryPath, str(self.path))
