#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import argparse
import os
import sys

from kast.utils.OsInfo import OsInfo, OsName


def _setupPlatformTweaks() -> None:
    if OsInfo.name == OsName.Windows:
        # Needed for console-less version [pythonw/Nuitka/PyInstaller]:
        stdnull = open(os.devnull, 'w')
        sys.stdout = sys.stdout if sys.stdout is not None else stdnull
        sys.stderr = sys.stderr if sys.stderr is not None else stdnull

        # Workaround for COM thread configuration interference with PyQt:
        from winrt import _winrt
        _winrt.uninit_apartment()

        # Workaround for QMediaPlayer using 'directshow' for backend instead of 'windowsmediafoundation':
        # (DirectShow has no support for proprietary codecs like 'h264'.)
        # (Requires: Qt>=5.15.5 Otherwise codec pack must be installed instead.)
        os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', help='enable debug mode', action='store_true')
    parser.add_argument('-r', '--recovery', help='enable recovery mode (some features will be disabled)', action='store_true')
    parsedArgs = parser.parse_args()

    _setupPlatformTweaks()

    from kast.KastApp import KastApp
    app = KastApp(
        debug=getattr(parsedArgs, 'debug'),
        recovery=getattr(parsedArgs, 'recovery')
    )
    sys.exit(app.run())


if __name__ == "__main__":
    main()
