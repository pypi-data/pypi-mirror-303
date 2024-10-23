#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from importlib.metadata import PackageNotFoundError, metadata


def _getMetadata() -> dict[str, str]:
    try:
        return {
            key: value[0] if isinstance(value, list) else value
            for key, value in metadata(__package__).json.items()
        }
    except PackageNotFoundError:
        return {}


__metadata = _getMetadata()

__version_info__: tuple[int, int, int] = (1, 4, 1)
__version__: str = '.'.join([str(i) for i in __version_info__])

__app_name__: str = __package__.capitalize()
__description__: str = __metadata.get('summary', '')
__app_url__: str = __metadata.get('project_url', '').split(',')[-1].strip()

__author_and_email: list[str] = __metadata.get(
    'author_email',
    '"" <>'
)[1:-1].split('" <')
__author__: str = __author_and_email[0]
__email__: str = __author_and_email[1]
