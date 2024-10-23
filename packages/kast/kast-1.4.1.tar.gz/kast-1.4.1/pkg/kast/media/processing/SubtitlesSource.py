#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABC, abstractmethod
from pathlib import Path

from kast.media.processing.MediaProcessingService import MediaProcessingService
from kast.media.processing.MetaData import SubtitleStreamInfo


class ISubtitlesSource(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def toVtt(self, mediaProcessingService: MediaProcessingService) -> Path:
        """Convert subtitles source to VTT format and provide result file path."""


class SubtitlesFromStream(ISubtitlesSource):

    def __init__(
        self,
        mediaFile: Path,
        streamInfo: SubtitleStreamInfo
    ) -> None:
        self._mediaFile = mediaFile
        self._streamId = streamInfo.id
        self._name = streamInfo.name

    @property
    def name(self) -> str:
        return self._name

    def toVtt(self, mediaProcessingService: MediaProcessingService) -> Path:
        return mediaProcessingService.extractSubtitles(
            inputFile=self._mediaFile,
            streamId=self._streamId
        )


class SubtitlesFromFile(ISubtitlesSource):

    def __init__(self, subtitlesFile: Path) -> None:
        self._subtitlesFile = subtitlesFile

    @property
    def name(self) -> str:
        return self._subtitlesFile.name

    def toVtt(self, mediaProcessingService: MediaProcessingService) -> Path:
        return mediaProcessingService.convertSubtitles(inputFile=self._subtitlesFile)
