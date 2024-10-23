#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import sys
import tempfile
from pathlib import Path

import psutil
import tendo.singleton


class SingletonApplication:

    def __init__(self, appName: str) -> None:
        try:
            self._appLock = tendo.singleton.SingleInstance(lockfile=self.establishLockFilePath(appName=appName))
        except tendo.singleton.SingleInstanceException:
            print(f"Application {appName} already running!")
            sys.exit(-1)

    @staticmethod
    def establishLockFilePath(appName: str) -> str:
        userName = psutil.Process().username().replace('\\', '-')
        return str(Path(tempfile.gettempdir()) / f"{appName}-{userName}-instance.lock")
