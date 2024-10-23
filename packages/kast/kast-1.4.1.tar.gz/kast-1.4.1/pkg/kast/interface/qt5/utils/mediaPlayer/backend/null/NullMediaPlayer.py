#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState
from kast.interface.qt5.utils.mediaPlayer.backend.common.MediaPlayerBase import MediaPlayerBase


class NullMediaPlayer(MediaPlayerBase):

    def init(self) -> None:
        pass  # Explicitly disables the subtitle engine!

    def shutdown(self) -> None:
        pass  # Explicitly disables the subtitle engine!

    def _onVolumeMutedChange(self, value: bool) -> None:
        pass

    def _onVolumeLevelChange(self, value: float) -> None:
        pass

    def _onStateChange(self, state: MediaPlayerState) -> None:
        super()._onStateChange(state=state)

        actions = {
            MediaPlayerState.Stopped: lambda: self._stopWatch.stop(),
            MediaPlayerState.Buffering: lambda: self._stopWatch.pause(),
            MediaPlayerState.Playing: lambda: self._stopWatch.start(),
            MediaPlayerState.Paused: lambda: self._stopWatch.pause(),
            MediaPlayerState.Seeking: lambda: self._stopWatch.stop(),
        }
        actions.get(state, lambda: None)()

        if state == MediaPlayerState.Seeking:
            self._mediaDetails.state = self._mediaDetails.startState
