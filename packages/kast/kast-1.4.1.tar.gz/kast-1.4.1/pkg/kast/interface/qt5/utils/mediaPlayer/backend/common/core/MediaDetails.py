#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from pathlib import Path

from PyQt5.QtCore import QObject
from PyQt5.QtMultimedia import QVideoSurfaceFormat
from tunit.unit import Milliseconds

from kast.interface.qt5.utils.mediaPlayer.MediaPlayerSignals import MediaPlayerSignals
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState
from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.IAudioService import AudioFormat
from kast.interface.qt5.utils.mediaPlayer.backend.common.utils.FpsReport import FpsReport
from kast.media.processing.common import StreamId
from kast.utils.StopWatch import StopWatch
from kast.utils.log.Loggable import Loggable


class MediaDetails(QObject, Loggable):

    DEFAULT_VOLUME_MUTED = False
    DEFAULT_VOLUME_LEVEL = 1.0

    DEFAULT_STREAM_ID = 0
    DEFAULT_START_POSITION = Milliseconds(0)
    DEFAULT_START_STATE = MediaPlayerState.Playing

    def __init__(
        self,
        signals: MediaPlayerSignals,
        positionTracker: StopWatch,
        parent: QObject | None = None
    ) -> None:
        super().__init__(parent=parent)

        self._signals: MediaPlayerSignals = signals

        self._positionTracker: StopWatch = positionTracker

        self._state = MediaPlayerState.Stopped

        self._volumeMuted: bool = self.DEFAULT_VOLUME_MUTED
        self._volumeLevel: float = self.DEFAULT_VOLUME_LEVEL

        self._mediaFilePath: Path | None = None
        self._videoStreamId: StreamId = self.DEFAULT_STREAM_ID
        self._audioStreamId: StreamId = self.DEFAULT_STREAM_ID
        self._startPosition: Milliseconds = self.DEFAULT_START_POSITION
        self._startState: MediaPlayerState = self.DEFAULT_START_STATE
        self._duration: Milliseconds = Milliseconds(0)

        self._surfaceFormat: QVideoSurfaceFormat | None = None
        self._audioFormat: AudioFormat | None = None

        self._fpsReport: FpsReport = FpsReport()

    @property
    def fpsReport(self) -> FpsReport:
        return self._fpsReport

    @property
    def position(self) -> Milliseconds:
        return self._startPosition + self._positionTracker.elapsed

    @property
    def volumeMuted(self) -> bool:
        return self._volumeMuted

    @volumeMuted.setter
    def volumeMuted(self, value: bool) -> None:
        self._volumeMuted = value
        self._signals.signalOnVolumeMutedChange.emit(value)

    @property
    def volumeLevel(self) -> float:
        return self._volumeLevel

    @volumeLevel.setter
    def volumeLevel(self, value: float) -> None:
        self._volumeLevel = value
        self._signals.signalOnVolumeLevelChange.emit(value)

    @property
    def state(self) -> MediaPlayerState:
        return self._state

    @state.setter
    def state(self, state: MediaPlayerState) -> None:
        if state == self._state:
            return

        self.log.info(f"State changed: {self._state} -> {state}")

        if state is MediaPlayerState.Stopped:
            self._startPosition = self.DEFAULT_START_POSITION
            self._startState = self.DEFAULT_START_STATE
            self.notifyPositionChanged(force=True)

        self._state = state
        self._signals.signalOnStateChange.emit(state)

    @property
    def mediaFilePath(self) -> Path | None:
        return self._mediaFilePath

    @mediaFilePath.setter
    def mediaFilePath(self, value: Path | None) -> None:
        if value != self._mediaFilePath:
            self._mediaFilePath = value
            self._videoStreamId = self.DEFAULT_STREAM_ID
            self._audioStreamId = self.DEFAULT_STREAM_ID
            self.state = MediaPlayerState.Stopped

    @property
    def videoStreamId(self) -> StreamId:
        return self._videoStreamId

    @videoStreamId.setter
    def videoStreamId(self, value: StreamId | None) -> None:
        self._videoStreamId = value if value is not None else self.DEFAULT_STREAM_ID

    @property
    def audioStreamId(self) -> StreamId:
        return self._audioStreamId

    @audioStreamId.setter
    def audioStreamId(self, value: StreamId | None) -> None:
        self._audioStreamId = value if value is not None else self.DEFAULT_STREAM_ID

    @property
    def startPosition(self) -> Milliseconds:
        return self._startPosition

    @startPosition.setter
    def startPosition(self, value: Milliseconds) -> None:
        self._startPosition = value

    @property
    def startState(self) -> MediaPlayerState:
        return self._startState

    @startState.setter
    def startState(self, value: MediaPlayerState) -> None:
        self._startState = value

    @property
    def duration(self) -> Milliseconds:
        return self._duration

    @duration.setter
    def duration(self, value: Milliseconds) -> None:
        self._duration = value
        self._signals.signalOnDurationChange.emit(int(value))

    @property
    def surfaceFormat(self) -> QVideoSurfaceFormat | None:
        return self._surfaceFormat

    @surfaceFormat.setter
    def surfaceFormat(self, value: QVideoSurfaceFormat | None) -> None:
        self._surfaceFormat = value

    @property
    def audioFormat(self) -> AudioFormat | None:
        return self._audioFormat

    @audioFormat.setter
    def audioFormat(self, value: AudioFormat | None) -> None:
        self._audioFormat = value

    def notifyPositionChanged(self, force: bool = False) -> None:
        if force or self._state is MediaPlayerState.Playing:
            self._signals.signalOnPositionChange.emit(int(self.position))

    def changeStateSilently(self, state: MediaPlayerState) -> None:
        self._state = state
