#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.IAudioService import IAudioService
from kast.utils.OsInfo import OsInfo, OsName


class AudioServiceFactory:

    @staticmethod
    def create(appName: str | None = None) -> IAudioService:
        if OsInfo.name == OsName.Linux:
            from .impl.SoundCardAudioService import SoundCardAudioService
            return SoundCardAudioService(appName=appName)

        from .impl.PyAudioAudioService import PyAudioAudioService
        return PyAudioAudioService()
