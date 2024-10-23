#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from PyQt5.QtGui import QOpenGLContext
from PyQt5.QtWidgets import QWidget

from kast.interface.qt5.utils.mediaPlayer.frontend.VideoSurfaceWidget import OpenGlVideoSurfaceWidget, \
    PaintEventHandler, \
    RasterVideoSurfaceWidget

VideoSurfaceWidget = OpenGlVideoSurfaceWidget | RasterVideoSurfaceWidget


class VideoSurfaceWidgetFactory:

    @classmethod
    def create(
        cls,
        paintEventHandler: PaintEventHandler,
        parent: QWidget | None
    ) -> VideoSurfaceWidget:
        videoSurfaceWidgetType: type[VideoSurfaceWidget] = OpenGlVideoSurfaceWidget if cls._isOpenGl() \
            else RasterVideoSurfaceWidget

        return videoSurfaceWidgetType(
            paintEventHandler=paintEventHandler,
            parent=parent
        )

    @staticmethod
    def _isOpenGl() -> bool:
        return QOpenGLContext().create()
