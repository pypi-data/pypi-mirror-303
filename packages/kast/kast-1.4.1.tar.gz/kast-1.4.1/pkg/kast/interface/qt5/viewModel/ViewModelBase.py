#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from typing import Any, Generic, Protocol, TypeVar

from PyQt5.QtCore import pyqtBoundSignal
from PyQt5.QtGui import QCloseEvent, QShowEvent

from kast.Services import Services
from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.utils.QtHelper import QtHelper


class ViewProtocol(Protocol):
    def setupUi(self, widget: Any) -> None: ...
    def show(self) -> None: ...


TViewProtocol = TypeVar('TViewProtocol', bound=ViewProtocol)


class ViewBase:
    @classmethod
    def createView(
        cls: type[TViewProtocol],
        hidden: bool = False,
        *args: Any,
        **kwargs: Any
    ) -> TViewProtocol:
        view: TViewProtocol = cls(*args, **kwargs)
        view.setupUi(view)
        if not hidden:
            view.show()
        return view


class DialogViewBase(ViewBase):
    signalOnOpen: pyqtBoundSignal = QtHelper.declareSignal()
    signalOnClose: pyqtBoundSignal = QtHelper.declareSignal()

    def reject(self) -> None:
        self.signalOnClose.emit()

    def showEvent(self, event: QShowEvent) -> None:
        self.signalOnOpen.emit()

    def closeEvent(self, event: QCloseEvent) -> None:
        event.ignore()
        self.signalOnClose.emit()


class ViewModelBase(Generic[TViewProtocol]):

    def __init__(self, uiServices: UiServices, view: TViewProtocol) -> None:
        self._uiServices: UiServices = uiServices
        self.__view: TViewProtocol = view

        self._uiServices.appLifecycleService.subscribeStartup(self._onStartup)
        self._uiServices.appLifecycleService.subscribeShutdown(self._onShutdown)

    @property
    def services(self) -> Services:
        return self._uiServices.services

    @property
    def uiServices(self) -> UiServices:
        return self._uiServices

    @property
    def view(self) -> TViewProtocol:
        return self.__view

    def _onStartup(self) -> None:
        pass

    def _onShutdown(self) -> None:
        pass
