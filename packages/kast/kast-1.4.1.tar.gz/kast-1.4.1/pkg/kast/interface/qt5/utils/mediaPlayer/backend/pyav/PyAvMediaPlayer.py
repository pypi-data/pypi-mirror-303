#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import dataclasses
from threading import Event

from PyQt5.QtCore import QObject, pyqtBoundSignal

from kast.interface.qt5.utils.QtHelper import QtHelper
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState
from kast.interface.qt5.utils.mediaPlayer.backend.common.MediaPlayerBase import MediaPlayerBase
from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.AudioServiceFactory import AudioServiceFactory
from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.IAudioService import IAudioService
from kast.interface.qt5.utils.mediaPlayer.backend.common.utils.FpsReport import FpsReport
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.Frame import AudioFrame, VideoFrame
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.core.LifecycleMonitor import LifecycleMonitor
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.core.PlayerStoppedException import PlayerStoppedException
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.workers.AudioWorker import AudioWorker
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.workers.BufferingWorker import BufferingWorker
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.workers.IWorker import IWorker
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.workers.SyncedThreadPool import SyncedThreadPool
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.workers.VideoWorker import VideoWorker
from kast.interface.qt5.utils.mediaPlayer.frontend.VideoSurface import VideoSurface
from kast.utils.FifoBuffer import FifoBuffer


class PyAvMediaPlayer(MediaPlayerBase):

    signalOnFpsReportUpdate: pyqtBoundSignal = QtHelper.declareSignal()

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

        self._audioService: IAudioService = AudioServiceFactory.create(
            appName=QtHelper.getApp().applicationName()
        )

        self._lifecycleMonitor: LifecycleMonitor = LifecycleMonitor(
            shutdownEvent=self._shutdownEvent,
            mediaDetails=self._mediaDetails
        )

        self._videoFrameBuffer: FifoBuffer[VideoFrame] = FifoBuffer()
        self._audioFrameBuffer: FifoBuffer[AudioFrame] = FifoBuffer()

        self._bufferingWorker: BufferingWorker = BufferingWorker(
            mediaDetails=self._mediaDetails,
            lifecycleMonitor=self._lifecycleMonitor,
            videoFrameBuffer=self._videoFrameBuffer,
            audioFrameBuffer=self._audioFrameBuffer
        )

        self._videoWorker: VideoWorker = VideoWorker(
            mediaDetails=self._mediaDetails,
            lifecycleMonitor=self._lifecycleMonitor,
            videoFrameBuffer=self._videoFrameBuffer,
            positionTracker=self._stopWatch,
            surface=self._surface
        )

        self._audioWorker: AudioWorker = AudioWorker(
            mediaDetails=self._mediaDetails,
            lifecycleMonitor=self._lifecycleMonitor,
            audioFrameBuffer=self._audioFrameBuffer,
            audioService=self._audioService
        )

        workers: list[IWorker] = [
            self._bufferingWorker,
            self._videoWorker,
            self._audioWorker
        ]
        self._syncedThreadPool: SyncedThreadPool = SyncedThreadPool(
            workers=workers,
            runWorkersCondition=self._lifecycleMonitor.shouldPlay,
            cleanupCallback=self._cleanupBeforeWorkers,
            exceptionHandler=self._workersExceptionHandler,
            shutdownEvent=self._shutdownEvent
        )

        self._videoWorker.signalFps.connect(lambda fps: self._updateFpsReport(fps))

    @property
    def fpsReport(self) -> FpsReport:
        return dataclasses.replace(self._mediaDetails.fpsReport)

    def init(self) -> None:
        """Starts all worker threads."""
        super().init()
        self._audioService.init()
        self._syncedThreadPool.start()

    def shutdown(self) -> None:
        """Shuts all worker threads."""
        super().shutdown()
        self._syncedThreadPool.stop()
        self._audioService.shutdown()

    def _onVolumeMutedChange(self, value: bool) -> None:
        self._audioService.setVolumeMuted(value=value)

    def _onVolumeLevelChange(self, value: float) -> None:
        self._audioService.setVolumeLevel(value=value)

    def _workersExceptionHandler(self, worker: str, ex: Exception) -> None:
        if not isinstance(ex, PlayerStoppedException):
            self.log.exception(f"Worker '{worker}' failed! Stopping player!", exc_info=ex)
            self._mediaDetails.state = MediaPlayerState.Stopped
            self._surface.reportError(errorMessage=str(ex))

    def _cleanupBeforeWorkers(self) -> None:
        if self._mediaDetails.state is MediaPlayerState.Seeking:
            self._mediaDetails.changeStateSilently(MediaPlayerState.Playing)

    def _updateFpsReport(self, backendFps: int) -> None:
        self._mediaDetails.fpsReport.backendFps = backendFps
        self._mediaDetails.fpsReport.frontendFps = self._surface.fps

        self.log.debug(f"Fps report: {self._mediaDetails.fpsReport}")

        self.signalOnFpsReportUpdate.emit()
