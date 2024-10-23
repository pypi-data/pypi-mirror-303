#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from PyQt5.QtCore import QObject, pyqtBoundSignal

from kast.interface.qt5.utils.QtHelper import QtHelper
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState


class MediaPlayerSignals(QObject):
    signalOnStateChange: pyqtBoundSignal = QtHelper.declareSignal(MediaPlayerState)
    signalOnDurationChange: pyqtBoundSignal = QtHelper.declareSignal(int)  # ms
    signalOnPositionChange: pyqtBoundSignal = QtHelper.declareSignal(int)  # ms
    signalOnVolumeMutedChange: pyqtBoundSignal = QtHelper.declareSignal(bool)
    signalOnVolumeLevelChange: pyqtBoundSignal = QtHelper.declareSignal(float)
