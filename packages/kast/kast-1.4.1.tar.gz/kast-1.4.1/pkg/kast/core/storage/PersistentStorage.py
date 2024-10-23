#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from pathlib import Path

from kast.core.AppInfo import AppInfo


class PersistentStorage:

    def __init__(self, appInfo: AppInfo) -> None:
        self._storagePath = Path.home() / f'.config/{appInfo.package}'
        self._storagePath.mkdir(parents=True, exist_ok=True)

    @property
    def path(self) -> Path:
        return self._storagePath
