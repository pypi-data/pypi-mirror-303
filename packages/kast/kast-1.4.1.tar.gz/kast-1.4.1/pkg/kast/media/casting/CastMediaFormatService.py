#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass
from enum import Enum

from kast.media.processing.MetaData import MetaData
from kast.media.processing.Resolution import FULL_HD, Resolution, ULTRA_HD
from kast.media.processing.common import CodecName, StreamId
from kast.utils.Maybe import Maybe


class StreamNotFoundException(Exception):
    pass


class VideoCodec(CodecName, Enum):
    H264 = 'h264'
    HEVC = 'hevc'  # 'h265'


class AudioCodec(CodecName, Enum):
    AC3 = 'ac3'
    EAC3 = 'eac3'
    AAC = 'aac'  # No evidence for wider support!


@dataclass(frozen=True)
class MediaContainerInfo:
    extension: str
    mimeType: str


class MediaContainer(MediaContainerInfo, Enum):
    MP4 = ('mp4', 'video/mp4')
    MKV = ('mkv', 'video/x-matroska')
    WEBM = ('webm', 'video/webm')


@dataclass(frozen=True)
class MediaFormatSupport:
    containers: list[MediaContainer]
    maxResolution: Resolution
    videoCodecs: list[CodecName]
    audioCodecs: list[CodecName]


@dataclass(frozen=True)
class CastDeviceInfo:
    model: str
    mediaFormatSupport: MediaFormatSupport


class CastDeviceProfile(CastDeviceInfo, Enum):
    CHROMECAST_3 = (
        'Chromecast 3',
        MediaFormatSupport(
            containers=[MediaContainer.MP4, MediaContainer.MKV],  # TODO: Check: 'webm'
            maxResolution=FULL_HD,
            videoCodecs=[VideoCodec.H264],
            audioCodecs=[AudioCodec.AC3, AudioCodec.EAC3]
        )
    )
    CHROMECAST_ULTRA_FULLHD = (
        'Chromecast Ultra (FullHD)',
        MediaFormatSupport(
            containers=[MediaContainer.MP4, MediaContainer.MKV],  # TODO: Check: 'webm'
            maxResolution=FULL_HD,
            videoCodecs=[VideoCodec.H264, VideoCodec.HEVC],
            audioCodecs=[AudioCodec.AC3, AudioCodec.EAC3]
        )
    )
    CHROMECAST_ULTRA_4K = (
        'Chromecast Ultra (4K)',
        MediaFormatSupport(
            containers=[MediaContainer.MP4, MediaContainer.MKV],  # TODO: Check: 'webm'
            maxResolution=ULTRA_HD,
            videoCodecs=[VideoCodec.HEVC],  # TODO: Verify: 'h264' & 4K
            audioCodecs=[AudioCodec.AC3, AudioCodec.EAC3]
        )
    )
    CHROMECAST_4_FULLHD = (
        'Chromecast 4 (FullHD)',
        MediaFormatSupport(
            containers=[MediaContainer.MP4, MediaContainer.MKV],  # TODO: Check: 'webm'
            maxResolution=FULL_HD,
            videoCodecs=[VideoCodec.H264, VideoCodec.HEVC],
            audioCodecs=[AudioCodec.AC3, AudioCodec.EAC3]
        )
    )
    CHROMECAST_4_4K = (
        'Chromecast 4 (4K)',
        MediaFormatSupport(
            containers=[MediaContainer.MP4, MediaContainer.MKV],  # TODO: Check: 'webm'
            maxResolution=ULTRA_HD,
            videoCodecs=[VideoCodec.H264, VideoCodec.HEVC],
            audioCodecs=[AudioCodec.AC3, AudioCodec.EAC3]
        )
    )


@dataclass(frozen=True)
class MediaInfo:
    container: str
    resolution: Resolution
    videoCodec: CodecName
    audioCodec: CodecName


class CastMediaFormatService:

    @classmethod
    def makeMediaInfo(
        cls,
        videoStreamId: StreamId,
        audioStreamId: StreamId,
        metaData: MetaData,
    ) -> MediaInfo:
        videoStream = Maybe(metaData.findVideoStreamById(streamId=videoStreamId))\
            .orThrow(lambda: StreamNotFoundException(f"Video stream by id '{videoStreamId}' not found!"))
        audioStream = Maybe(metaData.findAudioStreamById(streamId=audioStreamId))\
            .orThrow(lambda: StreamNotFoundException(f"Audio stream by id '{audioStreamId}' not found!"))
        return MediaInfo(
            container=metaData.containerType.lower(),
            resolution=videoStream.resolution,
            videoCodec=videoStream.codecName.lower(),
            audioCodec=audioStream.codecName.lower(),
        )

    @classmethod
    def shouldChangeContainer(
        cls,
        mediaInfo: MediaInfo,
        profile: CastDeviceProfile
    ) -> bool:
        containerTypes = [container.extension for container in profile.mediaFormatSupport.containers]
        return mediaInfo.container not in containerTypes

    @classmethod
    def shouldChangeResolution(
        cls,
        mediaInfo: MediaInfo,
        profile: CastDeviceProfile
    ) -> bool:
        return mediaInfo.resolution > profile.mediaFormatSupport.maxResolution

    @classmethod
    def shouldChangeVideoCodec(
        cls,
        mediaInfo: MediaInfo,
        profile: CastDeviceProfile
    ) -> bool:
        return mediaInfo.videoCodec not in profile.mediaFormatSupport.videoCodecs

    @classmethod
    def shouldChangeAudioCodec(
        cls,
        mediaInfo: MediaInfo,
        profile: CastDeviceProfile
    ) -> bool:
        return mediaInfo.audioCodec not in profile.mediaFormatSupport.audioCodecs
