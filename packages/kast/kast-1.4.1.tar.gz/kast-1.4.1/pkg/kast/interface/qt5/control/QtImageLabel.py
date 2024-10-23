#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QResizeEvent
from PyQt5.QtWidgets import QLabel, QWidget

from kast.utils.Maybe import Maybe


class QtImageLabel(QLabel):

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent=parent)

        self._pixmap: QPixmap | None = None

        self.setScaledContents(False)

    def sizeHint(self) -> QSize:
        width: int = self.width()
        return QSize(width, self._calcHeight())

    def setPixmap(self, pixmap: QPixmap) -> None:
        self._pixmap = pixmap
        self._updatePixmap()

    def resizeEvent(self, event: QResizeEvent) -> None:
        Maybe(self._pixmap).ifPresent(lambda _: self._updatePixmap())

    def _updatePixmap(self) -> None:
        super().setPixmap(self._scaledPixmap())

    def _calcHeight(self) -> int:
        return Maybe(self._pixmap)\
            .map(lambda pixmap: int((pixmap.height() * self.width()) / pixmap.width()))\
            .orElseGet(lambda: self.height())

    def _scaledPixmap(self) -> QPixmap:
        if self._pixmap is None:
            return QPixmap()

        return self._pixmap.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
