#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from pathlib import Path

from PyQt5.QtCore import QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QImage, QPaintEvent, QPainter, QPixmap, QRegion, QResizeEvent
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from .VideoSurface import VideoSurface
from .VideoSurfaceWidgetFactory import VideoSurfaceWidgetFactory


class VideoWidget(QWidget):

    def __init__(
        self,
        logoPath: Path | None = None,
        displayFps: bool = False,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(parent=parent)

        self._logoPath: Path | None = logoPath
        self._displayFps: bool = displayFps

        self._surfaceWidget = VideoSurfaceWidgetFactory.create(
            paintEventHandler=self._paint,
            parent=self
        )
        self._surface = VideoSurface(self._surfaceWidget)

        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.addWidget(self._surfaceWidget)

    @property
    def surface(self) -> VideoSurface:
        return self._surface

    @property
    def displayFps(self) -> bool:
        return self._displayFps

    @displayFps.setter
    def displayFps(self, value: bool) -> None:
        self._displayFps = value

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)

        self._surface.updateVideoRect(repaint=True)

    def _paint(self, event: QPaintEvent) -> None:
        with QPainter(self._surfaceWidget) as painter:
            try:
                painter.setRenderHint(QPainter.SmoothPixmapTransform)

                if not self._surface.isActive():
                    self._paintIdle(painter=painter, event=event)
                    return

                self._paintFrame(painter=painter, event=event)
                self._surface.paint(painter)

            finally:
                self._paintErrorMessage(painter=painter)
                if self._displayFps:
                    self._paintFps(painter=painter)

    def _paintIdle(self, painter: QPainter, event: QPaintEvent) -> None:
        painter.fillRect(event.rect(), self._surfaceWidget.backgroundColor)

        if self._logoPath is not None:
            self._paintLogo(painter=painter)

    def _paintLogo(self, painter: QPainter) -> None:
        logo = QImage(str(self._logoPath))

        logoSize = logo.size()
        deviceSize = QSize(painter.device().width(), painter.device().height())
        logoSize.scale(logoSize.boundedTo(deviceSize), Qt.KeepAspectRatio)

        targetRect = QRect(QPoint(0, 0), logoSize)
        deviceRect = QRect(QPoint(0, 0), deviceSize)

        targetRect.moveCenter(deviceRect.center())

        painter.drawPixmap(targetRect, QPixmap.fromImage(logo), logo.rect())

    def _paintFrame(self, painter: QPainter, event: QPaintEvent) -> None:
        videoRect = self._surface.videoRect
        if videoRect.contains(event.rect()):
            return

        region = event.region()
        region = region.subtracted(QRegion(videoRect))

        brush = self._surfaceWidget.backgroundColor
        for rect in region.rects():
            painter.fillRect(rect, brush)

    def _paintFps(self, painter: QPainter) -> None:
        painter.save()

        fontSize = int(self.height() / 14)

        font = painter.font()
        font.setPointSize(fontSize)
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(Qt.darkYellow)

        painter.drawText(self.rect(), int(Qt.AlignTop | Qt.AlignRight), f"{self._surface.fps} ")

        painter.restore()

    def _paintErrorMessage(self, painter: QPainter) -> None:
        errorMessage = self._surface.errorMessage
        if not errorMessage:
            return

        painter.save()

        fontSize = int(self.height() / 40)

        font = painter.font()
        font.setPointSize(fontSize)
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(Qt.darkRed)

        fullRect = self.rect()
        writeAreaRect = QRect(
            fullRect.x(),
            fullRect.y(),
            int(fullRect.width() * 0.8),
            fullRect.height()
        )

        flags = int(Qt.AlignTop | Qt.AlignLeft | Qt.TextWordWrap)
        painter.drawText(writeAreaRect, flags, errorMessage)

        painter.restore()
