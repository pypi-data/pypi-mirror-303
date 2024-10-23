#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABC, abstractmethod
from dataclasses import dataclass

from numpy.typing import NDArray
from tunit.unit import Milliseconds


@dataclass
class AudioFormat:
    sampleRate: int
    sampleSizeBits: int
    sampleSizeBytes: int
    channelCount: int


class IAudioService(ABC):

    @property
    @abstractmethod
    def latency(self) -> Milliseconds:
        pass

    @abstractmethod
    def isVolumeMuted(self) -> bool:
        pass

    @abstractmethod
    def setVolumeMuted(self, value: bool) -> None:
        pass

    @abstractmethod
    def getVolumeLevel(self) -> float:
        pass

    @abstractmethod
    def setVolumeLevel(self, value: float) -> None:
        pass

    @abstractmethod
    def setAudioFormat(self, audioFormat: AudioFormat) -> None:
        pass

    @abstractmethod
    def init(self) -> None:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def enqueueFrame(self, data: NDArray) -> None:
        pass
