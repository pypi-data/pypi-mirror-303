[![PyPI pyversions](https://img.shields.io/pypi/pyversions/kast.svg)](https://pypi.python.org/pypi/kast)
[![PyPI version shields.io](https://img.shields.io/pypi/v/kast.svg)](https://pypi.python.org/pypi/kast)
[![PyPI license](https://img.shields.io/pypi/l/kast.svg)](https://pypi.python.org/pypi/kast)
[![Downloads](https://static.pepy.tech/badge/kast)](https://pepy.tech/project/kast)

# Kast

Seamlessly cast your local video files to chromecast type devices.
Regardless of media containers, codecs or subtitle formats.

## Features:

- Detect cast devices in your local network.
- Cast video files compliant with chromecast supported formats withou any extra steps.
- Automatically transcode and remux incompatible video files before casting.
- Automatically convert subtitles.
- Display local preview of streamed video.
- Thanks to the OS media integration, control your stream with a regular remote media control applications intended for your platform.
(e.g. KDE Connect for Plasma linux desktop)

## Supported platforms:

- Linux
- Windows

(Might work on others, but it's untested.)

## Supported devices:

- Chromecast 4
- Chromecast Ultra
- Chromecast 3

(Might work with others, but it's untested.)

## Local preview backends:

| Engine | Supported platforms | Required setup to achieve full functionality                                                                                                                                        | Notes                                          |
|--------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| Null   | All                 | -                                                                                                                                                                                   | Just a mock. Does not provide audio nor video. |
| PyAV   | Linux, Windows      | -                                                                                                                                                                                   | Aimed to be the default on all platforms.      |
| WinRT  | Windows             | Installation of some proprietary codecs (like HEVC). Codecs must be compatible with Windows Media Foundation.                                                                       | Aimed to be phased out.                        |
| Qt     | All                 | Installation of multiple codecs. </br>On Linux GStreamer codecs. </br>On Windows either DirectShow (default PyPI release) or Windows Media Foundation (default for binary release). | Aimed to be phased out.                        |

## Installation:

### Binary release:
- Linux Arch - Available at AUR under name `kast-bin`.
- Linux Generic - Download installation script from [here](https://bitbucket.org/massultidev/kast/downloads/).
- Windows - Download installer from [here](https://bitbucket.org/massultidev/kast/downloads/).

### PyPI release:
For satisfying user experience it is recommended to install the application in a separate virtual environment.
You can use your favorite env creation method like conda or venv.

Installation from PyPI using venv:
```sh
python -m venv /path/to/your/venv
cd /path/to/your/venv
source bin/activate
python -m pip install kast
```

## Changelog:

- Version: 1.40
    - Added support for 4K streaming.
    - Enabled PyAV based local player for Windows.
    - Cast device search provides results on the go and is interruptable.
    - Local player reports internal engine errors on screen.
    - Added recovery mode.
    - Resolved window flickering on open.
    - Improved background threading with scheduling.
    - GStreamer codecs are no longer bundled which caused crashes on Linux.
    - Binary releases no longer bundles python and scripts but actually compiles to a native binary.
- Version: 1.3.0
    - Alternative local player backend. (Experimental)(Windows)
    - Made new experimental local player backends into defaults. (Linux/Windows)
    - Improved local player backend switching stability.
    - Improved logger performance by making all prints non-blocking.
    - Dropped support for: Python < 3.10
- Version: 1.2.0
    - Local player subtitles support.
    - Option to disable local player.
    - Alternative local player backend. (Experimental)(Linux)
    - Improved subtitles extraction and conversions.
    - Improved performance and stability of the UI.
- Version: 1.1.1
    - Silent fail with 4K videos fixed. - Most chromecast devices support resolution up to Full HD. All videos are now converted to satisfy that constraint. Full support for 4K devices coming in the future.
- Version: 1.1.0
    - Taskbar progress support. (Windows/Linux)
    - Taskbar preview media controls. (Windows)

## FAQ:

### Local preview does not seem to work (video/audio/both issue).

- First go to: `Application > Settings > Local Player Backend`</br>
- Then try to choose a different backend.</br>
- If PyAV backend is available on your platform, it should be the best option.</br>
- If problem persists try to install codecs on your OS:
    - Linux - Install GStreamer codecs.
    - Windows:
        - Install codecs compatible with Windows Media Foundation. Most notably HEVC codec. Should be available in MS Store.
        - Install codecs compatible with DirectShow. Some codec pack like K-Lite should be enough.

### I see no progress on taskbar on Linux.

Taskbar progress on Linux is supported only by selected desktop environments. (Like KDE or Unity.)

Furthermore, the application would have to be installed in either of root or user environment.

However, both approaches are discouraged and binary installation is recommended.

If you don't want the binary package, please use venv like so:
```sh
# Copy desktop and icon files to user environment:
cp -fv ${your_venv_prefix}/share/applications/* ~/.local/share/applications/
cp -fv ${your_venv_prefix}/share/pixmaps/* ~/.local/share/pixmaps/

# Create launcher script:
echo "#!/usr/bin/sh" > ~/.local/bin/kast
echo "source ${your_venv_prefix}/bin/activate" >> ~/.local/bin/kast
echo "python -m kast" >> ~/.local/bin/kast
chmod +x ~/.local/bin/kast

# Remember to replace all occurrences of the "${your_venv_prefix}" with an actual path to your venv directory!
```

## License
MIT
