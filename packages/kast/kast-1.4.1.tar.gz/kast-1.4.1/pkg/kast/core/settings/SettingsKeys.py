#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from PyQt5.QtCore import QStandardPaths
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerFactory import MediaPlayerFactory
from kast.utils.OsInfo import OsInfo, OsName

DefaultValueFactory = Callable[[], str | None]


def defaultBrowseMediaPath() -> Path:
    fallbackPath = Path.home() if OsInfo.name != OsName.Windows\
        else Path(Path.home().anchor)

    return [Path(path) for path in (
        list(QStandardPaths.standardLocations(QStandardPaths.MoviesLocation))
        + [fallbackPath]
    )][0]


@dataclass(frozen=True)
class SettingsKey:
    key: str
    defaultValueFactory: DefaultValueFactory = field(default=lambda: None)

    def __hash__(self) -> int:
        return hash(self.key)


class SettingsKeys(Enum):
    PreviousTemporaryPath = SettingsKey('media.path.temporary')
    BrowseMediaPath = SettingsKey(
        'media.path.browsing',
        lambda: str(defaultBrowseMediaPath())
    )
    MediaPreviewBackendEngine = SettingsKey(
        'media.preview.backend.engine',
        lambda: MediaPlayerFactory.getDefaultBackend().value
    )
