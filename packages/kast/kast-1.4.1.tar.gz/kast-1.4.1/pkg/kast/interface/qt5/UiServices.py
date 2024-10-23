#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.Services import Services
from kast.interface.qt5.service.AppLifecycleService import AppLifecycleService
from kast.interface.qt5.service.MediaControlService import MediaControlService
from kast.interface.qt5.service.UiEventObserver import UiEventObserver
from kast.interface.qt5.service.UiStateService import UiStateService
from kast.interface.qt5.utils.dialog.DialogService import DialogService
from kast.interface.qt5.utils.threading.ThreadContext import ThreadContext
from kast.interface.qt5.utils.threading.foreground.ForegroundScheduler import ForegroundScheduler
from kast.utils.functional import ErrorHandler
from kast.utils.threading.Scheduler import Scheduler


class UiServices:

    def __init__(self, services: Services, onBackgroundError: ErrorHandler | None = None) -> None:
        self.services = services

        self.foregroundScheduler = ForegroundScheduler()
        self.backgroundScheduler = Scheduler(executorCount=4, errorHandler=onBackgroundError)

        self.threadContext = ThreadContext(
            foregroundScheduler=self.foregroundScheduler,
            backgroundScheduler=self.backgroundScheduler
        )

        self.dialogService = DialogService(foregroundThreadContext=self.threadContext)

        self.appLifecycleService = AppLifecycleService()
        self.uiEventObserver = UiEventObserver()
        self.uiStateService = UiStateService(
            foregroundThreadContext=self.threadContext,
            uiEventObserver=self.uiEventObserver,
            castEventObserver=self.services.castEventObserver
        )
        self.mediaControlService = MediaControlService(
            services=services,
            threadContext=self.threadContext,
            dialogService=self.dialogService,
            uiStateService=self.uiStateService
        )
