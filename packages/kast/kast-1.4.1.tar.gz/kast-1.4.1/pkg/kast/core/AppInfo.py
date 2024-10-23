#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from pathlib import Path

from kast import __app_name__, __author__, __description__, __email__, __package__, __version__
from kast.utils.ResourceProvider import ResourceProvider


class AppInfo:

    _MISSING_INFO: str = '---'

    def __init__(self, resourceProvider: ResourceProvider) -> None:
        self._resourceProvider = resourceProvider

    @property
    def author(self) -> str:
        return __author__ or self._MISSING_INFO

    @property
    def email(self) -> str:
        return __email__ or self._MISSING_INFO

    @property
    def package(self) -> str:
        return __package__ or self._MISSING_INFO

    @property
    def appName(self) -> str:
        return __app_name__ or self._MISSING_INFO

    @property
    def appVersion(self) -> str:
        return __version__ or self._MISSING_INFO

    @property
    def appDescription(self) -> str:
        return __description__ or self._MISSING_INFO

    @property
    def desktopFileName(self) -> str:
        return f'{__package__}.desktop'

    @property
    def appIconPath(self) -> Path:
        return self._resourceProvider.getResourcePath('kast.png')
