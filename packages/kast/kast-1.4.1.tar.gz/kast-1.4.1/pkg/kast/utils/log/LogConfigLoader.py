#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from __future__ import annotations  # TODO: Remove when support dropped for: Python < ?

import logging.config
from pathlib import Path

import yaml

from kast.utils.DeepUpdateableDict import DeepUpdateableDict

ReplaceMap = dict[str, str]


class LogConfigLoader:

    def __init__(self) -> None:
        self._config: DeepUpdateableDict = DeepUpdateableDict()

    def apply(self) -> None:
        logging.config.dictConfig(self._config)

    def loadYmlIf(
        self,
        condition: bool,
        filePath: Path,
        replaceMap: ReplaceMap | None = None
    ) -> LogConfigLoader:
        return self if not condition\
            else self.loadYml(filePath=filePath, replaceMap=replaceMap)

    def loadYml(
        self,
        filePath: Path,
        replaceMap: ReplaceMap | None = None
    ) -> LogConfigLoader:
        replaceMap = replaceMap if replaceMap is not None else {}

        ymlStr = self._readFile(filePath)\
            .format(**replaceMap)

        config = yaml.safe_load(ymlStr)
        self._config.deepUpdate(config)

        return self

    @staticmethod
    def _readFile(filePath: Path) -> str:
        with open(filePath) as f:
            return f.read()
