#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from enum import Enum, unique

from PyQt5.QtCore import QObject

from kast.interface.qt5.utils.mediaPlayer.IMediaPlayer import IMediaPlayer
from kast.interface.qt5.utils.mediaPlayer.backend.null.NullMediaPlayer import NullMediaPlayer
from kast.interface.qt5.utils.mediaPlayer.frontend.VideoSurface import VideoSurface
from kast.utils.OsInfo import OsInfo, OsName


@unique
class MediaPlayerBackend(Enum):
    Null = 'null'
    Qt = 'qt'
    PyAV = 'pyav'
    WinRt = 'winrt'


class MediaPlayerFactory:

    _IGNORE_PLATFORM_RESTRICTIONS: bool = False

    _PLATFORM_DEPENDENT_BACKENDS = {
        OsName.Linux: [MediaPlayerBackend.PyAV],
        OsName.Windows: [MediaPlayerBackend.PyAV, MediaPlayerBackend.WinRt],
    }

    @classmethod
    def getDefaultBackend(cls) -> MediaPlayerBackend:
        return cls.getSupportedBackends()[0]

    @classmethod
    def getSupportedBackends(cls) -> list[MediaPlayerBackend]:
        return cls._PLATFORM_DEPENDENT_BACKENDS.get(OsInfo.name, []) + [
            MediaPlayerBackend.Qt,
            MediaPlayerBackend.Null,
        ]

    @classmethod
    def create(
        cls,
        backend: MediaPlayerBackend,
        surface: VideoSurface,
        feignMode: bool = False,
        parent: QObject | None = None
    ) -> IMediaPlayer:
        if feignMode:
            return NullMediaPlayer(surface=surface, parent=parent)

        if(
            not cls._IGNORE_PLATFORM_RESTRICTIONS and
            backend not in cls.getSupportedBackends()
        ):
            raise RuntimeError(f"Media player backend '{backend}' is not supported on platform '{OsInfo.name}'!")

        if backend == MediaPlayerBackend.PyAV:
            from kast.interface.qt5.utils.mediaPlayer.backend.pyav.PyAvMediaPlayer import PyAvMediaPlayer
            return PyAvMediaPlayer(surface=surface, parent=parent)

        if backend == MediaPlayerBackend.WinRt:
            from kast.interface.qt5.utils.mediaPlayer.backend.winrt.WinRtMediaPlayer import WinRtMediaPlayer
            return WinRtMediaPlayer(surface=surface, parent=parent)

        if backend == MediaPlayerBackend.Qt:
            from kast.interface.qt5.utils.mediaPlayer.backend.qt.QtMediaPlayer import QtMediaPlayer
            return QtMediaPlayer(surface=surface, parent=parent)

        return NullMediaPlayer(surface=surface, parent=parent)
