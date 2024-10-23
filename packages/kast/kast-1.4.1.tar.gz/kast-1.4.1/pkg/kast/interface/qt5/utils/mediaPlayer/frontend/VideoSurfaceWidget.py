#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPaintEvent, QPalette
from PyQt5.QtWidgets import QOpenGLWidget, QSizePolicy, QWidget

PaintEventHandler = Callable[[QPaintEvent], None]

DEFAULT_BACKGROUND_COLOR = QColor(Qt.black)


class AbstractVideoSurfaceWidget:

    def __init__(
        self,
        renderer: str,
        widget: QWidget,
        paintEventHandler: PaintEventHandler,
        backgroundColor: QColor = DEFAULT_BACKGROUND_COLOR
    ) -> None:
        self._renderer: str = renderer
        self._widget: QWidget = widget
        self._paintEventHandler: PaintEventHandler = paintEventHandler
        self._backgroundColor = backgroundColor

        self._initUi()

    @property
    def renderer(self) -> str:
        return self._renderer

    @property
    def backgroundColor(self) -> QColor:
        return self._widget.palette().color(QPalette.Background)

    def paintEvent(self, event: QPaintEvent) -> None:
        self._paintEventHandler(event)

    def _initUi(self) -> None:
        self._widget.setAttribute(Qt.WA_NoSystemBackground, True)

        palette = self._widget.palette()
        palette.setColor(QPalette.Background, self._backgroundColor)
        self._widget.setPalette(palette)
        self._widget.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)


class RasterVideoSurfaceWidget(AbstractVideoSurfaceWidget, QWidget):
    def __init__(
        self,
        paintEventHandler: PaintEventHandler,
        backgroundColor: QColor = DEFAULT_BACKGROUND_COLOR,
        parent: QWidget | None = None
    ) -> None:
        QWidget.__init__(self, parent=parent)
        AbstractVideoSurfaceWidget.__init__(
            self,
            renderer="Raster",
            widget=self,
            paintEventHandler=paintEventHandler,
            backgroundColor=backgroundColor
        )


class OpenGlVideoSurfaceWidget(AbstractVideoSurfaceWidget, QOpenGLWidget):
    def __init__(
        self,
        paintEventHandler: PaintEventHandler,
        backgroundColor: QColor = DEFAULT_BACKGROUND_COLOR,
        parent: QWidget | None = None
    ) -> None:
        QOpenGLWidget.__init__(self, parent=parent)
        AbstractVideoSurfaceWidget.__init__(
            self,
            renderer="OpenGL",
            widget=self,
            paintEventHandler=paintEventHandler,
            backgroundColor=backgroundColor
        )
