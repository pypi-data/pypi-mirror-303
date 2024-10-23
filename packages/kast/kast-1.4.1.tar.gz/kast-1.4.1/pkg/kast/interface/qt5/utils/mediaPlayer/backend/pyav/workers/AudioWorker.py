#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import time

from tunit.unit import Seconds

from kast.interface.qt5.utils.mediaPlayer.backend.common.audio.IAudioService import IAudioService
from kast.interface.qt5.utils.mediaPlayer.backend.common.core.MediaDetails import MediaDetails
from kast.interface.qt5.utils.mediaPlayer.backend.common.utils.FrameDropTracker import FrameDropTracker
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.core.LifecycleMonitor import LifecycleMonitor
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.core.MPConstant import MPConstant
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.workers.FrameHandlingWorkerBase import FrameHandlingWorkerBase
from kast.utils.FifoBuffer import FifoBuffer


class AudioWorker(FrameHandlingWorkerBase):

    def __init__(
        self,
        mediaDetails: MediaDetails,
        lifecycleMonitor: LifecycleMonitor,
        audioFrameBuffer: FifoBuffer,
        audioService: IAudioService
    ) -> None:
        super().__init__(
            mediaDetails=mediaDetails,
            lifecycleMonitor=lifecycleMonitor,
            frameDropTracker=FrameDropTracker(frameTypeName='Audio')
        )

        self._audioFrameBuffer: FifoBuffer = audioFrameBuffer
        self._audioService: IAudioService = audioService

    @property
    def name(self) -> str:
        return 'AudioThread'

    def run(self) -> None:
        try:
            while self._mediaDetails.audioFormat is None:
                self._lifecycleMonitor.verifyNotStopped()
                time.sleep(MPConstant.SLEEP_WHILE_WAITING.toRawUnit(unit=Seconds))

            self._audioService.setAudioFormat(audioFormat=self._mediaDetails.audioFormat)
            self._audioService.play()

            while not self._lifecycleMonitor.shouldStop():
                frame = self._audioFrameBuffer.tryGet(timeout=MPConstant.SLEEP_WHILE_WAITING)
                if frame is not None and self._shouldPlayFrame(frame=frame, offset=self._audioService.latency):
                    self._audioService.enqueueFrame(data=frame.data)

        finally:
            self._audioService.stop()

    def cleanup(self) -> None:
        self._audioFrameBuffer.clear()

        self._mediaDetails.audioFormat = None
