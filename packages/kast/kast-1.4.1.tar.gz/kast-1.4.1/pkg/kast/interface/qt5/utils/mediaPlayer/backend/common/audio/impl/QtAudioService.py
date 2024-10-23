#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from enum import Enum
from types import TracebackType

from PyQt5.QtCore import QByteArray, QDataStream, QIODevice, QObject, QThread
from PyQt5.QtMultimedia import QAudio, QAudioFormat, QAudioOutput
from numpy.typing import NDArray
from tunit.unit import Milliseconds

from kast.interface.qt5.utils.QtAbc import QtAbc
from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.IAudioService import AudioFormat
from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.impl.AudioServiceBase import AudioServiceBase, \
    IAudioOutput
from kast.utils.log.Loggable import Loggable


class AudioError(Enum):
    NoError = QAudio.Error.NoError
    OpenError = QAudio.Error.OpenError
    IOError = QAudio.Error.IOError
    UnderrunError = QAudio.Error.UnderrunError
    FatalError = QAudio.Error.FatalError


class AudioState(Enum):
    ActiveState = QAudio.State.ActiveState
    SuspendedState = QAudio.State.SuspendedState
    StoppedState = QAudio.State.StoppedState
    IdleState = QAudio.State.IdleState
    InterruptedState = QAudio.State.InterruptedState


class QtAudioOutput(IAudioOutput, Loggable):

    def __init__(
        self,
        audioFormat: AudioFormat,
        parent: QObject | None = None
    ) -> None:
        self._parent: QObject | None = parent
        self._audioFormat: AudioFormat = audioFormat

        self._audioOutput: QAudioOutput | None = None
        self._outputDevice: QIODevice | None = None

    def __enter__(self) -> IAudioOutput:
        qAudioFormat = QAudioFormat()
        qAudioFormat.setChannelCount(self._audioFormat.channelCount)
        qAudioFormat.setSampleRate(self._audioFormat.sampleRate)
        qAudioFormat.setSampleSize(self._audioFormat.sampleSizeBits)
        qAudioFormat.setCodec("audio/pcm")
        qAudioFormat.setSampleType(QAudioFormat.SampleType.Float)

        self._audioOutput = output = QAudioOutput(qAudioFormat, self._parent)
        output.stateChanged.connect(lambda state: self._onCoreStateChange(output=output, state=state))
        output.setVolume(1.0)

        self.log.debug("Starting 'Qt' audio output...")

        self._outputDevice = output.start()

        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> None:
        self.log.debug("Stopping 'Qt' audio output...")

        output = self._audioOutput
        if output is not None:
            output.stop()
            output.reset()
            output.stateChanged.disconnect()

    @property
    def latency(self) -> Milliseconds:
        return Milliseconds()

    def writeFrame(self, frame: NDArray) -> None:
        outputDevice = self._outputDevice
        if outputDevice is not None:
            outPustStream = QDataStream(outputDevice)
            outPustStream << QByteArray(self._adjustVolume(frame).tobytes())  # type: ignore

    def _onCoreStateChange(self, output: QAudioOutput, state: QAudio.State) -> None:
        stateEnum = AudioState(state)
        self.log.info(f'Core state: {stateEnum}[{stateEnum.value}]')

        error = AudioError(output.error())
        if error != AudioError.NoError:
            self.log.error(f'Core error: {error.name}[{error.value}]')


class QtAudioService(QtAbc, QObject, AudioServiceBase, Loggable):  # Does not work on Linux!

    def __init__(self) -> None:
        super().__init__()
        self.__thread: QThread | None = None

    def init(self) -> None:
        if self.__thread is None:
            self.__thread = thread = QThread()
            self.moveToThread(thread)
            thread.started.connect(self._run)
            thread.start()

    def shutdown(self) -> None:
        thread = self.__thread
        if thread is not None:
            self._shutdownEvent.set()
            thread.quit()
            thread.wait()
            self.__thread = None

            self._reset()

    def _createAudioOutputContextManager(self, audioFormat: AudioFormat) -> IAudioOutput:
        return QtAudioOutput(audioFormat=audioFormat, parent=self)
