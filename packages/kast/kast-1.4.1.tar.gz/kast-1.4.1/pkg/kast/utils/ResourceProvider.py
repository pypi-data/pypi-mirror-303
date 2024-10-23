#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from pathlib import Path
from types import ModuleType


class ResourceProvider:

    def __init__(self, package: ModuleType, assetsDirName: str = 'assets') -> None:
        self.assetsDir = Path(str(package.__file__)).parent / assetsDirName

    def getResourcePath(self, assetRelativePath: Path | str) -> Path:
        return self.assetsDir / assetRelativePath
