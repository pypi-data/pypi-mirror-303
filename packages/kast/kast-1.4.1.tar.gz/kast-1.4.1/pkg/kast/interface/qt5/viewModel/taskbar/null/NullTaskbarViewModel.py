#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.interface.qt5.viewModel.taskbar.common.TaskbarViewModelBase import TaskbarViewModelBase


class NullTaskbarViewModel(TaskbarViewModelBase):

    def _displayProgress(self, display: bool, percentage: float = 0.0) -> None:
        pass
