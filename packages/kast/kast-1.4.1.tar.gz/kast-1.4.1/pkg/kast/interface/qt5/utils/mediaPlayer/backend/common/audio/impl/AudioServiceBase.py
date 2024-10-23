#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from __future__ import annotations  # TODO: Remove when support dropped for: Python < ?

import math
import time
from abc import ABC, abstractmethod
from threading import Event, Thread
from types import TracebackType

import numpy
from numpy.typing import NDArray
from tunit.unit import Milliseconds, Nanoseconds, Seconds

from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.IAudioService import AudioFormat, IAudioService
from kast.utils.FifoBuffer import FifoBuffer
from kast.utils.log.Loggable import Loggable


class IAudioOutput(ABC):

    @abstractmethod
    def __enter__(self) -> IAudioOutput: ...
    @abstractmethod
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> None: ...

    @property
    @abstractmethod
    def latency(self) -> Milliseconds: ...
    @abstractmethod
    def writeFrame(self, frame: NDArray) -> None: ...


class AudioServiceBase(IAudioService, Loggable):  # Does not work on Windows!

    _IDLE_DELAY: Milliseconds = Milliseconds(20)
    _COOLDOWN_DELAY: Nanoseconds = Nanoseconds(1)
    _DEFAULT_SHOULD_PLAY: bool = False
    _DEFAULT_LATENCY: Milliseconds = Milliseconds()

    def __init__(self) -> None:
        self._frameBuffer: FifoBuffer[NDArray] = FifoBuffer()
        self._audioFormat: AudioFormat | None = None
        self._thread: Thread | None = None

        self._shutdownEvent: Event = Event()
        self._audioFormatChangeEvent: Event = Event()

        self._shouldPlay: bool = self._DEFAULT_SHOULD_PLAY

        self._latency: Milliseconds = self._DEFAULT_LATENCY
        self._volumeLevel: float = 1.0
        self._volumeMuted: bool = False

    @property
    def latency(self) -> Milliseconds:
        return self._latency

    def isVolumeMuted(self) -> bool:
        return self._volumeMuted

    def setVolumeMuted(self, value: bool) -> None:
        self._volumeMuted = value

    def getVolumeLevel(self) -> float:
        return self._volumeLevel

    def setVolumeLevel(self, value: float) -> None:
        self._volumeLevel = value

    def setAudioFormat(self, audioFormat: AudioFormat) -> None:
        if audioFormat != self._audioFormat:
            self._reset(audioFormat=audioFormat)
            self._audioFormatChangeEvent.set()

    def init(self) -> None:
        if self._thread is None:
            self._thread = Thread(
                target=self._run,
                name=self.__class__.__name__,
                daemon=True
            )
            self._thread.start()

    def shutdown(self) -> None:
        if self._thread is not None:
            self._shutdownEvent.set()
            self._thread.join()
            self._thread = None

            self._reset()

    def play(self) -> None:
        self._shouldPlay = True

    def stop(self) -> None:
        self._shouldPlay = False

    def enqueueFrame(self, data: NDArray) -> None:
        self._frameBuffer.tryPut(item=data)

    def _adjustVolume(self, frame: NDArray) -> NDArray:
        if self._volumeMuted:
            return numpy.zeros(frame.shape)

        multiplier = math.pow(2, (math.sqrt(math.sqrt(math.sqrt(self._volumeLevel))) * 192 - 192)/6)
        return numpy.multiply(frame, multiplier, casting="unsafe")

    def _reset(self, audioFormat: AudioFormat | None = None) -> None:
        self._audioFormat = audioFormat
        self._frameBuffer.clear()
        self._shouldPlay = self._DEFAULT_SHOULD_PLAY

    def _playerLoop(self, audioOutput: IAudioOutput) -> None:
        try:
            while(
                not self._shutdownEvent.is_set()
                and not self._audioFormatChangeEvent.is_set()
            ):
                time.sleep(self._COOLDOWN_DELAY.toRawUnit(unit=Seconds))

                self._latency = audioOutput.latency

                if not self._shouldPlay:
                    time.sleep(self._IDLE_DELAY.toRawUnit(unit=Seconds))
                    continue

                frame = self._frameBuffer.tryGet(timeout=self._COOLDOWN_DELAY)
                if frame is not None:
                    audioOutput.writeFrame(frame=self._adjustVolume(frame))

        finally:
            self._latency = self._DEFAULT_LATENCY
            self._audioFormatChangeEvent.clear()

    def _run(self) -> None:
        self.log.info(f"{self.__class__.__name__} started.")
        try:
            while not self._shutdownEvent.is_set():
                try:
                    time.sleep(self._COOLDOWN_DELAY.toRawUnit(unit=Seconds))

                    audioFormat = self._audioFormat
                    if audioFormat is None:
                        time.sleep(self._IDLE_DELAY.toRawUnit(unit=Seconds))
                        continue

                    with self._createAudioOutputContextManager(audioFormat=audioFormat) as audioOutput:
                        self._playerLoop(audioOutput=audioOutput)

                except Exception as ex:
                    self.log.exception(ex)
                    self._audioFormat = None

        finally:
            self._audioFormatChangeEvent.clear()
            self._shutdownEvent.clear()
            self.log.info(f"{self.__class__.__name__} stopped.")

    @abstractmethod
    def _createAudioOutputContextManager(self, audioFormat: AudioFormat) -> IAudioOutput: ...
