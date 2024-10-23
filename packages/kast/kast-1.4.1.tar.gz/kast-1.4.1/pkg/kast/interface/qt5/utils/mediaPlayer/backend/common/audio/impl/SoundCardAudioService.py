#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from types import TracebackType
from typing import Protocol

import soundcard
from numpy.typing import NDArray
from tunit.unit import Milliseconds, Seconds

from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.IAudioService import AudioFormat
from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.impl.AudioServiceBase import AudioServiceBase, \
    IAudioOutput
from kast.utils.OsInfo import OsInfo, OsName
from kast.utils.log.Loggable import Loggable


class PlayerCore(Protocol):  # Protocol for type: 'soundcard.Player'

    def __enter__(self) -> IAudioOutput: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> None: ...

    @property
    def latency(self) -> float: ...
    def play(self, frame: NDArray) -> None: ...


class SoundCardAudioOutput(IAudioOutput, Loggable):

    def __init__(self, audioFormat: AudioFormat) -> None:
        self._audioFormat: AudioFormat = audioFormat

        self._player: PlayerCore | None = None

    def __enter__(self) -> IAudioOutput:
        player = soundcard.default_speaker().player(
            samplerate=self._audioFormat.sampleRate,
            channels=self._audioFormat.channelCount
        )

        self.log.debug("Starting 'SoundCard' audio output...")

        self._player = player.__enter__()

        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> None:
        self.log.debug("Stopping 'SoundCard' audio output...")

        player = self._player
        if player is not None:
            return player.__exit__(exc_type, exc_val, exc_tb)

    @property
    def latency(self) -> Milliseconds:
        player = self._player
        return Milliseconds() if OsInfo.name != OsName.Linux or player is None\
            else Milliseconds.fromRawUnit(unit=Seconds, value=player.latency)

    def writeFrame(self, frame: NDArray) -> None:
        player = self._player
        if player is not None:
            player.play(frame)


class SoundCardAudioService(AudioServiceBase, Loggable):  # Does not work on Windows!

    def __init__(
        self,
        appName: str | None = None
    ) -> None:
        super().__init__()

        if OsInfo.name == OsName.Linux:
            soundcard.set_name(appName if appName is not None else 'Python')

    def _createAudioOutputContextManager(self, audioFormat: AudioFormat) -> IAudioOutput:
        return SoundCardAudioOutput(audioFormat=audioFormat)
