#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import asyncio
from collections.abc import Callable
from dataclasses import dataclass
from datetime import timedelta
from pathlib import Path
from threading import Event, Thread
from typing import cast

import numpy
from PyQt5.QtCore import QObject, QSize
from PyQt5.QtGui import QImage
from PyQt5.QtMultimedia import QAbstractVideoBuffer, QVideoFrame, QVideoSurfaceFormat
from numpy.typing import NDArray
from tunit.unit import Milliseconds, Seconds
from winrt.windows.foundation import EventRegistrationToken
from winrt.windows.graphics.imaging import BitmapAlphaMode, BitmapBufferAccessMode, BitmapDecoder, BitmapPixelFormat, \
    SoftwareBitmap
from winrt.windows.media import VideoFrame
from winrt.windows.media.core import MediaSource
from winrt.windows.media.editing import MediaClip, MediaComposition, VideoFramePrecision
from winrt.windows.media.mediaproperties import MediaEncodingProfile
from winrt.windows.media.playback import MediaPlaybackSession, MediaPlaybackState, MediaPlayer, \
    MediaPlayerFailedEventArgs
from winrt.windows.storage import StorageFile
from winrt.windows.storage.streams import InMemoryRandomAccessStream, RandomAccessStream

from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState
from kast.interface.qt5.utils.mediaPlayer.backend.common.MediaPlayerBase import MediaPlayerBase
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.core.MPConstant import MPConstant
from kast.interface.qt5.utils.mediaPlayer.frontend.VideoSurface import VideoSurface
from kast.utils.FifoBuffer import FifoBuffer
from kast.utils.Maybe import Maybe
from kast.utils.pathUtils import fileExtension

_Task = Callable[[], None]


@dataclass
class _VideoFormat:
    pixelFormat: BitmapPixelFormat
    width: int
    height: int


@dataclass
class _CoreSubscription:
    token: EventRegistrationToken
    unsubscriber: Callable[[EventRegistrationToken], None]

    def unsubscribe(self) -> None:
        self.unsubscriber(self.token)


class WinRtMediaPlayer(MediaPlayerBase):

    _DEFAULT_PLAYER_STATE = MediaPlayerState.Stopped
    _STATE_MAPPING = {
        MediaPlaybackState.NONE: MediaPlayerState.Stopped,
        MediaPlaybackState.OPENING: MediaPlayerState.Buffering,
        MediaPlaybackState.BUFFERING: MediaPlayerState.Buffering,
        MediaPlaybackState.PLAYING: MediaPlayerState.Playing,
        MediaPlaybackState.PAUSED: MediaPlayerState.Paused,
    }

    def __init__(
        self,
        surface: VideoSurface,
        parent: QObject | None = None
    ) -> None:
        super().__init__(
            surface=surface,
            parent=parent
        )

        self._shutdownEvent: Event = Event()
        self._stopEvent: Event = Event()
        self._stateTaskQueue: FifoBuffer[_Task] = FifoBuffer()
        self._frameTaskQueue: FifoBuffer[_Task] = FifoBuffer()
        self._threads: list[Thread] = []

        self._coreSubscriptions: list[_CoreSubscription] = []

        self._maybeCore: Maybe[MediaPlayer] = Maybe()

    @property
    def _coreState(self) -> MediaPlayerState:
        return self._maybeCore.map(lambda core: core.playback_session)\
            .map(lambda session: session.playback_state)\
            .map(lambda state: self._STATE_MAPPING.get(state))\
            .orElse(self._DEFAULT_PLAYER_STATE)

    def init(self) -> None:
        super().init()

        threads = self._threads
        if len(threads) > 0:
            return

        def createThread(name: str, taskQueue: FifoBuffer[_Task]) -> Thread:
            return Thread(
                target=lambda: self._taskLoop(taskQueue=taskQueue),
                daemon=True,
                name=name
            )

        self._shutdownEvent.clear()
        threads = [
            createThread(name='StateHandlerThread', taskQueue=self._stateTaskQueue),
            createThread(name='FrameHandlerThread', taskQueue=self._frameTaskQueue),
        ]
        for thread in threads:
            thread.start()

        self._threads = threads

    def shutdown(self) -> None:
        super().shutdown()

        threads = self._threads
        if len(threads) <= 0:
            return

        self._shutdownEvent.set()
        self._shutdownCore()

        for thread in threads:
            thread.join()

        self._threads = []

    def _initCore(self) -> None:
        if self._maybeCore.isPresent():
            return

        mediaFilePath = self._mediaDetails.mediaFilePath
        if mediaFilePath is None:
            self.log.error('Cannot init player core without media file path!')
            return

        videoFormat = asyncio.run(self._getVideoFormat(mediaFilePath=mediaFilePath))

        core = MediaPlayer()
        coreSubscriptions: list[_CoreSubscription] = []

        core.command_manager.is_enabled = False
        core.is_video_frame_server_enabled = True

        coreSubscriptions.append(_CoreSubscription(
            token=core.add_media_failed(lambda sender, event: self._onCoreError(event=event)),
            unsubscriber=core.remove_media_failed
        ))

        core.is_muted = self._mediaDetails.volumeMuted
        core.volume = self._mediaDetails.volumeLevel

        def queueFrame(sender: MediaPlayer) -> None:
            self._frameTaskQueue.tryPut(lambda: asyncio.run(self._onCoreFrameChange(sender, videoFormat)))
        coreSubscriptions.append(_CoreSubscription(
            token=core.add_video_frame_available(lambda sender, args: queueFrame(sender=sender)),
            unsubscriber=core.remove_video_frame_available
        ))

        playbackSession: MediaPlaybackSession = core.playback_session
        coreSubscriptions.append(_CoreSubscription(
            token=playbackSession.add_playback_state_changed(lambda session, args: self._onCoreStateChange(session=session)),
            unsubscriber=playbackSession.remove_playback_state_changed
        ))
        coreSubscriptions.append(_CoreSubscription(
            token=playbackSession.add_natural_duration_changed(lambda session, args: self._onCoreDurationChange(session=session)),
            unsubscriber=playbackSession.remove_natural_duration_changed
        ))
        coreSubscriptions.append(_CoreSubscription(
            token=playbackSession.add_seek_completed(lambda session, args: self._onCoreSeekCompleted()),
            unsubscriber=playbackSession.remove_seek_completed
        ))

        size = QSize(
            videoFormat.width,
            videoFormat.height
        )
        self._mediaDetails.surfaceFormat = surfaceFormat = QVideoSurfaceFormat(size, QVideoFrame.PixelFormat.Format_RGB32)
        self._surface.start(surfaceFormat)

        core.source = MediaSource.create_from_storage_file(asyncio.run(self._openFile(mediaFilePath)))

        self._coreSubscriptions = coreSubscriptions
        self._maybeCore = Maybe(core)

        self._stopEvent.clear()

    def _shutdownCore(self) -> None:
        maybeCore = self._maybeCore
        if maybeCore.isEmpty():
            return

        self._maybeCore = Maybe()
        self._stopEvent.set()

        queues: list[FifoBuffer[_Task]] = [
            self._frameTaskQueue,
            self._stateTaskQueue,
        ]
        for queue in queues:
            queue.clear()

        coreSubscriptions, self._coreSubscriptions = self._coreSubscriptions, []
        for subscription in coreSubscriptions:
            subscription.unsubscribe()

        core = cast(MediaPlayer, maybeCore.value)
        core.close()

        self._surface.stop()

        # No longer receiving events! Need to clean up:
        self._stopWatch.stop()
        self._signals.signalOnDurationChange.emit(0)

    def _onVolumeMutedChange(self, value: bool) -> None:
        self._maybeCore.asPropertyAssigner().is_muted = value

    def _onVolumeLevelChange(self, value: float) -> None:
        self._maybeCore.asPropertyAssigner().volume = value

    def _onStateChange(self, state: MediaPlayerState) -> None:
        super()._onStateChange(state=state)

        self._stateTaskQueue.tryPut(lambda: self._handleState(state=state))

    def _handleState(self, state: MediaPlayerState) -> None:
        coreState = self._coreState
        if state == coreState:
            return

        self._initCore()

        action = {
            MediaPlayerState.Stopped: self._handleStop,
            MediaPlayerState.Buffering: self._handleBuffer,
            MediaPlayerState.Playing: self._handlePlay,
            MediaPlayerState.Paused: self._handlePause,
            MediaPlayerState.Seeking: self._handleSeek,
        }
        action.get(state, lambda: None)()

    def _handleStop(self) -> None:
        self._stopWatch.stop()
        self._shutdownCore()

    def _handleBuffer(self) -> None:
        self._stopWatch.pause()

    def _handlePlay(self) -> None:
        self._stopWatch.start()
        self._maybeCore.ifPresent(lambda core: core.play())

    def _handlePause(self) -> None:
        self._stopWatch.pause()
        self._maybeCore.ifPresent(lambda core: core.pause())

    def _handleSeek(self) -> None:
        self._stopWatch.stop()
        self._maybeCore.map(lambda core: core.playback_session)\
            .asPropertyAssigner()\
            .position = self._toTimeDelta(self._mediaDetails.position)

    def _onCoreError(self, event: MediaPlayerFailedEventArgs) -> None:
        self.log.error('Core error! Details:', event)

    def _onCoreStateChange(self, session: MediaPlaybackSession) -> None:
        coreState = session.playback_state
        state = self._STATE_MAPPING[coreState]
        self.log.info(f'Core state changed to: {state.name} (native={coreState.name}[{coreState.value}])')

    def _onCoreDurationChange(self, session: MediaPlaybackSession) -> None:
        duration = self._toMilliseconds(session.natural_duration)
        self.log.info(f'Core detected duration: {duration}')
        self._mediaDetails.duration = duration

    def _onCoreSeekCompleted(self) -> None:
        startState = self._mediaDetails.startState
        self.log.info(f'Core seek completed! Applying requested start state: {startState.name}')
        self._mediaDetails.state = startState

    async def _onCoreFrameChange(self, mediaPlayer: MediaPlayer, format: _VideoFormat) -> None:
        if self._stopEvent.is_set() or self._shutdownEvent.is_set():
            return

        try:
            videoFrameData = await self._getVideoFrameMatrix(mediaPlayer=mediaPlayer, format=format)
            qFrame = self._convertToQtFrame(videoFrameData=videoFrameData, format=format)
            self._presentFrame(qFrame=qFrame)

        except Exception:
            self.log.exception('Error:')

    def _presentFrame(self, qFrame: QVideoFrame) -> None:
        if not qFrame.map(QAbstractVideoBuffer.ReadOnly):
            raise RuntimeError("Couldn't map frame as read only!")

        self._surface.present(frame=qFrame)

    def _convertToQtFrame(self, videoFrameData: NDArray, format: _VideoFormat) -> QVideoFrame:
        qImage = QImage(
            cast(bytes, videoFrameData),
            format.width,
            format.height,
            QImage.Format.Format_RGBA8888
        )
        qImage.convertTo(QImage.Format.Format_RGB32)
        return QVideoFrame(qImage)

    async def _getVideoFrameMatrix(self, mediaPlayer: MediaPlayer, format: _VideoFormat) -> NDArray:
            with VideoFrame.create_as_direct3_d11_surface_backed(
                format.pixelFormat,
                format.width,
                format.height
            ) as frame:
                with frame.direct3_d_surface as direct3DSurface:
                    mediaPlayer.copy_frame_to_video_surface(direct3DSurface)

                    with await SoftwareBitmap.create_copy_from_surface_async(
                        frame.direct3_d_surface
                    ) as softwareBitmap:
                        with SoftwareBitmap.convert(
                            softwareBitmap,
                            BitmapPixelFormat.RGBA8,
                            BitmapAlphaMode.STRAIGHT
                        ) as convertedBitmap:
                            with convertedBitmap.lock_buffer(
                                BitmapBufferAccessMode.READ
                            ) as buffer:
                                with buffer.create_reference() as memoryBufferRef:
                                    return numpy.frombuffer(memoryBufferRef).copy()

    @classmethod
    async def _logMediaCodecs(cls, mediaFilePath: Path) -> None:
        mediaEncodingProfile = await MediaEncodingProfile.create_from_file_async(await cls._openFile(mediaFilePath))
        container = fileExtension(filePath=mediaFilePath).lower()
        audioCodec = mediaEncodingProfile.audio.subtype
        videoCodec = mediaEncodingProfile.video.subtype
        cls.log.info(f"Media info: {container=}, {audioCodec=}, {videoCodec=}")

    @classmethod
    async def _getVideoFormat(cls, mediaFilePath: Path) -> _VideoFormat:
        await cls._logMediaCodecs(mediaFilePath=mediaFilePath)
        mediaClip = await MediaClip.create_from_file_async(await cls._openFile(mediaFilePath))

        mediaComposition = MediaComposition()
        mediaComposition.clips.append(mediaClip)

        with await mediaComposition.get_thumbnail_async(
            cls._toTimeDelta(Milliseconds(0)),
            0,
            0,
            VideoFramePrecision.NEAREST_FRAME
        ) as thumbnailImageStream:
            with InMemoryRandomAccessStream() as inMemoryRandomAccessStream:

                await RandomAccessStream.copy_async(thumbnailImageStream, inMemoryRandomAccessStream)
                inMemoryRandomAccessStream.seek(0)

                bitmapDecoder = await BitmapDecoder.create_async(inMemoryRandomAccessStream)
                with await bitmapDecoder.get_software_bitmap_async() as softwareBitmap:
                    return _VideoFormat(
                        pixelFormat=softwareBitmap.bitmap_pixel_format,
                        width=softwareBitmap.pixel_width,
                        height=softwareBitmap.pixel_height
                    )

    @staticmethod
    async def _openFile(filePath: Path) -> StorageFile:
        return await StorageFile.get_file_from_path_async(str(filePath))

    @staticmethod
    def _toTimeDelta(milliseconds: Milliseconds = Milliseconds()) -> timedelta:
        return timedelta(milliseconds=int(milliseconds))

    @staticmethod
    def _toMilliseconds(timeSpan: timedelta) -> Milliseconds:
        return Milliseconds.fromRawUnit(unit=Seconds, value=timeSpan.total_seconds())

    def _taskLoop(self, taskQueue: FifoBuffer[_Task]) -> None:
        while not self._shutdownEvent.is_set():
            try:
                task = taskQueue.tryGet(timeout=MPConstant.SLEEP_WHILE_WAITING)
                if task is not None:
                    task()

            except Exception as ex:
                self.log.exception(ex)
                self._surface.reportError(errorMessage=str(ex))
                self._mediaDetails.state = MediaPlayerState.Stopped
