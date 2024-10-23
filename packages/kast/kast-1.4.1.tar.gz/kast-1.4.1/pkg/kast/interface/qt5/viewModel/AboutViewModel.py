#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QWidget

from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.view.AboutView import Ui_AboutView
from kast.interface.qt5.viewModel.ViewModelBase import ViewBase, ViewModelBase


class View(ViewBase, QDialog, Ui_AboutView):
    pass


class AboutViewModel(ViewModelBase[View]):

    def __init__(self, parent: QWidget, uiServices: UiServices) -> None:
        super().__init__(uiServices=uiServices, view=View.createView(hidden=True, parent=parent))

        logo = QPixmap(str(self.services.appInfo.appIconPath)).scaled(128, 128)
        self.view.labelLogo.setPixmap(logo)

        self.view.labelAppName.setText(self.services.appInfo.appName)
        self.view.labelAppVersion.setText(self.services.appInfo.appVersion)
        self.view.labelAppDescription.setText(self.services.appInfo.appDescription)
        self.view.labelAuthorName.setText(self.services.appInfo.author)
        self.view.labelAuthorContact.setText(self.services.appInfo.email)

        self.view.layout().activate()
        self.view.setFixedSize(self.view.size().width(), self.view.size().height())
