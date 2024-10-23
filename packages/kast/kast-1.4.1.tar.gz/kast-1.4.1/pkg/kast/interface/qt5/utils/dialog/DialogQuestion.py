#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from typing import cast

from PyQt5.QtWidgets import QMessageBox

ButtonId = int


class DialogQuestion:

    def __init__(
        self,
        title: str,
        message: str,
        default: bool = False,
        icon: QMessageBox.Icon = QMessageBox.Question,
        positiveButton: ButtonId = QMessageBox.Ok,
        negativeButton: ButtonId = QMessageBox.Cancel
    ) -> None:
        self._positiveButton = positiveButton
        self._negativeButton = negativeButton
        self._msgBox = msgBox = QMessageBox()

        msgBox.setIcon(icon)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(cast(QMessageBox.StandardButtons, positiveButton | negativeButton))
        msgBox.setDefaultButton(cast(QMessageBox.StandardButton, positiveButton if default else negativeButton))

    def display(self) -> bool:
        return self._msgBox.exec() == self._positiveButton

    def dismiss(self) -> None:
        self._msgBox.close()
