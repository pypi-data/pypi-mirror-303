#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from mpris_api.adapter.IMprisAdapterRoot import IMprisAdapterRoot

from kast.Services import Services
from kast.core.AppInfo import AppInfo


class MprisAdapterRoot(IMprisAdapterRoot):

    def __init__(self, services: Services) -> None:
        self._services: Services = services

    @property
    def _appInfo(self) -> AppInfo:
        return self._services.appInfo

    def canRaise(self) -> bool:
        return False  # TODO: Should we support that?

    def canQuit(self) -> bool:
        return False  # TODO: Should we support that?

    def canSetFullscreen(self) -> bool:
        return False  # TODO: Should we support that?

    def getIdentity(self) -> str:
        return self._appInfo.appName

    def getDesktopEntry(self) -> str | None:
        return str(self._services.resourceProvider.getResourcePath(self._appInfo.desktopFileName))

    def getSupportedUriSchemes(self) -> list[str]:
        return ['file']

    def getSupportedMimeTypes(self) -> list[str]:
        return ['video/*']

    def hasTracklist(self) -> bool:
        return False

    def isFullScreen(self) -> bool:
        return False  # TODO: Should we support that?

    def setFullScreen(self, value: bool) -> None:
        pass  # TODO: Should we support that?

    def quitApp(self) -> None:
        pass  # TODO: Should we support that?

    def raiseApp(self) -> None:
        pass  # TODO: Should we support that?
