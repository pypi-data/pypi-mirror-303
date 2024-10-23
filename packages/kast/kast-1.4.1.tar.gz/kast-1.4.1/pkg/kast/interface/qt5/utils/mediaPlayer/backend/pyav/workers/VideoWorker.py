#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import time

from PyQt5.QtCore import pyqtBoundSignal
from tunit.unit import Seconds

from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.Frame import VideoFrame
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.core.LifecycleMonitor import LifecycleMonitor
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.core.MPConstant import MPConstant
from kast.interface.qt5.utils.mediaPlayer.backend.common.core.MediaDetails import MediaDetails
from kast.interface.qt5.utils.mediaPlayer.backend.common.utils.FpsCounter import FpsCounter
from kast.interface.qt5.utils.mediaPlayer.backend.common.utils.FrameDropTracker import FrameDropTracker
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.workers.FrameHandlingWorkerBase import FrameHandlingWorkerBase
from kast.interface.qt5.utils.mediaPlayer.frontend.VideoSurface import VideoSurface
from kast.utils.FifoBuffer import FifoBuffer
from kast.utils.StopWatch import StopWatch


class VideoWorker(FrameHandlingWorkerBase):

    def __init__(
        self,
        mediaDetails: MediaDetails,
        lifecycleMonitor: LifecycleMonitor,
        videoFrameBuffer: FifoBuffer,
        positionTracker: StopWatch,
        surface: VideoSurface
    ) -> None:
        super().__init__(
            mediaDetails=mediaDetails,
            lifecycleMonitor=lifecycleMonitor,
            frameDropTracker=FrameDropTracker(frameTypeName='Video')
        )

        self._videoFrameBuffer: FifoBuffer = videoFrameBuffer
        self._positionTracker: StopWatch = positionTracker
        self._surface: VideoSurface = surface

        self._fpsCounter: FpsCounter = FpsCounter()

    @property
    def name(self) -> str:
        return 'VideoThread'

    @property
    def signalFps(self) -> pyqtBoundSignal:
        return self._fpsCounter.signalFps

    def run(self) -> None:
        try:
            self._handleBuffering()

            surfaceFormat = self._mediaDetails.surfaceFormat
            if surfaceFormat is None:
                self.log.critical("Surface format is null!")
                return
            if not self._surface.start(surfaceFormat):
                self.log.critical("Could not start the surface!")
                return

            self._mediaDetails.state = self._mediaDetails.startState

            while not self._lifecycleMonitor.shouldStop():
                frame = self._videoFrameBuffer.tryGet(timeout=MPConstant.SLEEP_WHILE_WAITING)
                if frame is None:
                    if self._videoFrameBuffer.isClosed:
                        self._mediaDetails.state = MediaPlayerState.Stopped
                        return

                    self._handleBuffering()
                    continue

                self._handlePause(frame=frame)
                self._handlePlay(frame=frame)

                time.sleep(MPConstant.SLEEP_TO_COOL_DOWN.toRawUnit(unit=Seconds))

        finally:
            self._positionTracker.stop()
            self._surface.stop()
            self._fpsCounter.reset()
            self._mediaDetails.notifyPositionChanged(force=True)

    def cleanup(self) -> None:
        self._videoFrameBuffer.clear()

        self._mediaDetails.surfaceFormat = None

    def _handleBuffering(self) -> None:
        self._positionTracker.pause()
        self._mediaDetails.state = MediaPlayerState.Buffering

        while not self._videoFrameBuffer.isFull:
            self._lifecycleMonitor.verifyNotStopped()
            time.sleep(MPConstant.SLEEP_WHILE_WAITING.toRawUnit(unit=Seconds))

        self._lifecycleMonitor.verifyNotStopped()

    def _handlePause(self, frame: VideoFrame) -> None:
        if self._mediaDetails.state is not MediaPlayerState.Paused:
            return

        self._positionTracker.pause()

        self._surface.present(frame=frame.frame)

        while self._mediaDetails.state is MediaPlayerState.Paused:
            self._lifecycleMonitor.verifyNotStopped()
            time.sleep(MPConstant.SLEEP_WHEN_IDLE.toRawUnit(unit=Seconds))

        self._lifecycleMonitor.verifyNotStopped()

    def _handlePlay(self, frame: VideoFrame) -> None:
        self._positionTracker.start()
        self._mediaDetails.state = MediaPlayerState.Playing

        if self._shouldPlayFrame(frame=frame):
            self._surface.present(frame=frame.frame)
            self._fpsCounter.tick()
