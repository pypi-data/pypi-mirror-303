#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABC

from PyQt5.QtWidgets import QMainWindow
from tunit.unit import Seconds

from kast.Services import Services
from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.service.UiEvent import UiEvent, UiState
from kast.interface.qt5.viewModel.taskbar.ITaskbarViewModel import ITaskbarViewModel
from kast.media.casting.model.CastState import CastMediaState
from kast.utils.threading.PeriodicRunner import PeriodicRunner


class TaskbarViewModelBase(ITaskbarViewModel, ABC):

    _UPDATE_INTERVAL: Seconds = Seconds(10)

    def __init__(
        self,
        parent: QMainWindow,
        uiServices: UiServices
    ) -> None:
        self._parent = parent
        self._uiServices = uiServices
        self._periodicUpdater: PeriodicRunner = PeriodicRunner(
            scheduler=self.uiServices.backgroundScheduler,
            interval=self._UPDATE_INTERVAL,
            runnable=lambda: self._updateProgress(uiEvent=uiServices.uiStateService.uiEvent)
        )

    @property
    def services(self) -> Services:
        return self._uiServices.services

    @property
    def uiServices(self) -> UiServices:
        return self._uiServices

    @property
    def _mediaState(self) -> CastMediaState:
        return self.uiServices.uiStateService.castState.mediaState

    def _updateProgress(self, uiEvent: UiEvent) -> None:
        if not uiEvent.progress.complete:
            percentageInt = uiEvent.progress.percentage
            percentageFloat = percentageInt / 100 if percentageInt is not None else 1.0
            self._displayProgress(True, percentageFloat)
            return

        duration = int(self._mediaState.duration)
        if (uiEvent.state == UiState.Streaming) and (duration > 0):
            self._periodicUpdater.start()
            self._displayProgress(True, int(self._mediaState.currentPosition)/duration)
            return

        self._periodicUpdater.stop()
        self._displayProgress(False)
