#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import platform
import signal
import sys
import threading
import types
from pathlib import Path

import setproctitle

from kast.Services import Services
from kast.core.AppRuntimeFlags import AppRuntimeFlags
from kast.interface.overlay.IMediaOverlay import IMediaOverlay
from kast.interface.overlay.MediaOverlayFactory import MediaOverlayFactory
from kast.interface.qt5.KastQtApp import KastQtApp
from kast.utils.OsInfo import OsInfo, OsName
from kast.utils.log.LogConfigLoader import LogConfigLoader
from kast.utils.log.Loggable import Loggable


class KastApp(Loggable):

    def __init__(
        self,
        debug: bool = False,
        recovery: bool = False
    ) -> None:
        self._services: Services = Services(appRuntimeFlags=AppRuntimeFlags(
            debug=debug,
            recovery=recovery
        ))
        self._osMediaOverlay: IMediaOverlay = MediaOverlayFactory.create(
            services=self._services,
            feignMode=recovery
        )
        self._desktopApp: KastQtApp = KastQtApp(services=self._services)

    def run(self) -> int:
        setproctitle.setproctitle(self._services.appInfo.appName)

        self._initLogger()
        self._initDebugCapabilities()

        signal.signal(signal.SIGTERM, self._onSignal)
        signal.signal(signal.SIGINT, self._onSignal)

        try:
            self.log.info("Application start!")
            self.log.info(f"Runtime flags: {self._services.appRuntimeFlags}")
            self.log.info(f"Platform name: {platform.platform()}")
            self.log.info(f"Detected OS: {OsInfo.name.value}")
            self.log.info(f"Python: {sys.version}")
            self.log.info(f"Interpreter path: '{sys.executable}'")
            self.log.info(f"Application: {self._services.appInfo.appName} ({self._services.appInfo.appVersion})")
            self.log.info(f"Persistent storage path: '{self._services.persistentStorage.path}'")
            self.log.info(f"Temporary storage path: '{self._services.temporaryStorage.path}'")

            self._services.temporaryStorage.cleanupArtifacts()

            self._services.mediaServer.mediaContent.thumbnailFile = self._services.appInfo.appIconPath
            self._services.mediaServer.start()
            self._osMediaOverlay.start()
            return self._desktopApp.run()

        except Exception as ex:
            self.log.exception(ex)
            return 1

        finally:
            self._onExit()

    def _onSignal(self, signum: int, frame: types.FrameType | None) -> None:
        self.log.info(f"Caught signal: {signal.Signals(signum).name}({signum})")
        self._desktopApp.exit(1)
        self._logActiveThreads()

    def _onExit(self) -> None:
        self._services.castController.disconnect()
        self._services.mediaServer.stop()
        self._osMediaOverlay.stop()
        self.log.info("Application shutdown!")
        self._logActiveThreads()

    def _logActiveThreads(self) -> None:
        self.log.debug(f'Still active thread count: {threading.active_count()}')
        for thr in threading.enumerate():
            self.log.debug(f'Still active thread info: {thr.name=}, {thr.daemon=}, {thr.native_id=}, {thr.ident=}')

    def _initDebugCapabilities(self) -> None:
        if not self._services.appRuntimeFlags.debug:
            return
        if OsInfo.name == OsName.Linux:
            try:
                import namedthreads
                namedthreads.patch()
            except Exception as ex:
                self.log.exception('Exposing thread names to OS failed!', ex)

    def _initLogger(self) -> None:
        logFilePath = self._services.persistentStorage.path / f'{self._services.appInfo.package}.log'
        LogConfigLoader()\
            .loadYml(
                filePath=self._getLogConfig('log-config.yml'),
                replaceMap={'logFilePath': str(logFilePath)}
            )\
            .loadYmlIf(
                condition=self._services.appRuntimeFlags.debug,
                filePath=self._getLogConfig('log-config-debug.yml')
            )\
            .apply()

    def _getLogConfig(self, name: str) -> Path:
        return self._services.resourceProvider.getResourcePath(assetRelativePath=name)
