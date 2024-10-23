#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABC, abstractmethod
from pathlib import Path

from tunit.unit import Milliseconds

from kast.interface.qt5.utils.mediaPlayer.MediaPlayerSignals import MediaPlayerSignals
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState


class IMediaPlayerSignals(ABC):

    @property
    @abstractmethod
    def signals(self) -> MediaPlayerSignals:
        pass


class IMediaPlayerAccessors(ABC):

    @abstractmethod
    def getState(self) -> MediaPlayerState:
        pass

    @abstractmethod
    def getDuration(self) -> Milliseconds:
        pass

    @abstractmethod
    def getPosition(self) -> Milliseconds:
        pass

    @abstractmethod
    def getVolumeMuted(self) -> bool:
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


class IMediaPlayerMethods(ABC):

    @abstractmethod
    def init(self) -> None:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass

    @abstractmethod
    def getMediaFile(self) -> Path | None:
        pass

    @abstractmethod
    def setMediaFile(self, mediaFilePath: Path | None = None) -> None:
        pass
        pass

    @abstractmethod
    def getSubtitleFile(self) -> Path | None:
        pass

    @abstractmethod
    def setSubtitleFile(self, subtitleFilePath: Path | None = None) -> None:
        pass

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def pause(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def seek(
        self,
        position: Milliseconds,
        play: bool | None = None
    ) -> None:
        pass


class IMediaPlayer(IMediaPlayerSignals, IMediaPlayerAccessors, IMediaPlayerMethods, ABC):

    @property
    def state(self) -> MediaPlayerState:
        return self.getState()

    @property
    def duration(self) -> Milliseconds:
        return self.getDuration()

    @property
    def position(self) -> Milliseconds:
        return self.getPosition()

    @property
    def volumeMuted(self) -> bool:
        return self.getVolumeMuted()

    @volumeMuted.setter
    def volumeMuted(self, value: bool) -> None:
        self.setVolumeMuted(value)

    @property
    def volumeLevel(self) -> float:
        return self.getVolumeLevel()

    @volumeLevel.setter
    def volumeLevel(self, value: float) -> None:
        self.setVolumeLevel(value)

    @property
    def mediaFile(self) -> Path | None:
        return self.getMediaFile()

    @mediaFile.setter
    def mediaFile(self, value: Path | None) -> None:
        self.setMediaFile(value)

    @property
    def subtitleFile(self) -> Path | None:
        return self.getSubtitleFile()

    @subtitleFile.setter
    def subtitleFile(self, value: Path | None) -> None:
        self.setSubtitleFile(value)
