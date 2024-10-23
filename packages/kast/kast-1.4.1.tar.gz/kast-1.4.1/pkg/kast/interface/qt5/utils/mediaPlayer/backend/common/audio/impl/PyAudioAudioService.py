#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass
from types import TracebackType

from numpy.typing import NDArray
from pyaudio import PyAudio, Stream as PyAudioStream
from tunit.unit import Milliseconds, Seconds

from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.IAudioService import AudioFormat
from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.impl.AudioServiceBase import AudioServiceBase, \
    IAudioOutput
from kast.utils.log.Loggable import Loggable


@dataclass
class _PyAudioCore:
    pyAudio: PyAudio
    stream: PyAudioStream


class PyAudioAudioOutput(IAudioOutput, Loggable):

    def __init__(self, audioFormat: AudioFormat) -> None:
        self._audioFormat: AudioFormat = audioFormat

        self._core: _PyAudioCore | None = None

    def __enter__(self) -> IAudioOutput:
        self.log.debug("Starting 'PyAudio' audio output...")

        pyAudio = PyAudio()
        stream = pyAudio.open(
            format=pyAudio.get_format_from_width(self._audioFormat.sampleSizeBytes),
            channels=self._audioFormat.channelCount,
            rate=self._audioFormat.sampleRate,
            output=True,
        )

        self._core = _PyAudioCore(
            pyAudio=pyAudio,
            stream=stream
        )

        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> None:
        self.log.debug("Stopping 'PyAudio' audio output...")

        core = self._core
        if core is not None:
            core.stream.stop_stream()
            core.stream.close()
            core.pyAudio.terminate()

    @property
    def latency(self) -> Milliseconds:
        core = self._core
        return Milliseconds() if core is None\
            else Milliseconds.fromRawUnit(unit=Seconds, value=core.stream.get_output_latency())

    def writeFrame(self, frame: NDArray) -> None:
        core = self._core
        if core is not None and not self._isZeroed(frame=frame):
            core.stream.write(frame.tobytes())

    def _isZeroed(self, frame: NDArray) -> bool:
        return not frame.any()


class PyAudioAudioService(AudioServiceBase, Loggable):  # Uses ALSA on Linux! (Setting app name not available!)

    def __init__(self) -> None:
        super().__init__()

    def _createAudioOutputContextManager(self, audioFormat: AudioFormat) -> IAudioOutput:
        return PyAudioAudioOutput(audioFormat=audioFormat)
