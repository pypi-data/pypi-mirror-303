#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass, field
from enum import Enum
from typing import TypeVar

from kast.media.processing.Resolution import Resolution
from kast.media.processing.common import CodecName, StreamId


class SubtitleStreamType(Enum):
    Unknown = 'unknown'
    Bitmap = 'bitmap'
    Text = 'text'
    Ass = 'ass'


@dataclass(frozen=True)
class StreamInfo:
    id: StreamId
    language: str | None
    title: str | None

    @property
    def name(self) -> str:
        return ' - '.join([
            segment for segment in [
                f'Stream {self.id}',
                self.language,
                self.title
            ]
            if segment is not None
        ])


@dataclass(frozen=True)
class MediaStreamInfo(StreamInfo):
    codecName: CodecName


@dataclass(frozen=True)
class AudioStreamInfo(MediaStreamInfo):
    pass


@dataclass(frozen=True)
class VideoStreamInfo(MediaStreamInfo):
    resolution: Resolution


@dataclass(frozen=True)
class SubtitleStreamInfo(StreamInfo):
    type: SubtitleStreamType = SubtitleStreamType.Unknown


TStreamInfo = TypeVar('TStreamInfo', bound=StreamInfo)


@dataclass(frozen=True)
class MetaData:
    title: str
    containerType: str
    videoStreams: list[VideoStreamInfo] = field(default_factory=lambda: [])
    audioStreams: list[AudioStreamInfo] = field(default_factory=lambda: [])
    subtitleStreams: list[SubtitleStreamInfo] = field(default_factory=lambda: [])

    def findVideoStreamById(self, streamId: StreamId) -> VideoStreamInfo | None:
        return self._findStreamById(streamId=streamId, streams=self.videoStreams)

    def findAudioStreamById(self, streamId: StreamId) -> AudioStreamInfo | None:
        return self._findStreamById(streamId=streamId, streams=self.audioStreams)

    def _findStreamById(
        self,
        streamId: StreamId,
        streams: list[TStreamInfo]
    ) -> TStreamInfo | None:
        for stream in streams:
            if stream.id == streamId:
                return stream

        return None
