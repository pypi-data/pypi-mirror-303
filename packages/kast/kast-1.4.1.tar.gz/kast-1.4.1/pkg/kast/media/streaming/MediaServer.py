#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J.

import contextlib
import socket
from dataclasses import dataclass
from pathlib import Path
from threading import Thread
from typing import cast

import bottle

from kast.media.streaming.ServerAdapter import ServerAdapter
from kast.utils.Maybe import Maybe
from kast.utils.log.Loggable import Loggable
from kast.utils.pathUtils import fileExtension
from kast.utils.typeUtils import castNotNull

IpV4Address = tuple[str, int]


@dataclass
class MediaContent:
    movieFile: Path | None = None
    subtitlesFile: Path | None = None
    thumbnailFile: Path | None = None


class MediaServer(Loggable):

    URL_MEDIA = '/media'
    URL_MOVIE = URL_MEDIA + '/movie'
    URL_SUBTITLES = URL_MEDIA + '/subtitles'
    URL_THUMBNAIL = URL_MEDIA + '/thumbnail'

    def __init__(self) -> None:
        self._serverAdapter: ServerAdapter | None = None
        self._webApp: bottle.Bottle | None = None

        self._thread: Thread | None = None

        self._mediaContent = MediaContent()

    def start(self) -> None:
        if self._thread is None:
            self._serverAdapter = self._getServerAdapter()
            self._webApp = bottle.Bottle()
            self._thread = thread = Thread(
                target=self._run,
                daemon=True,
                name=self.__class__.__name__
            )
            thread.start()

    def stop(self) -> None:
        Maybe(self._webApp).ifPresent(lambda webApp: webApp.close())  # type: ignore
        self._webApp = None

        Maybe(self._serverAdapter).ifPresent(lambda serverAdapter: serverAdapter.stop())
        self._serverAdapter = None

        Maybe(self._thread).ifPresent(lambda thread: thread.join())
        self._thread = None

    @property
    def mediaContent(self) -> MediaContent:
        return self._mediaContent

    @property
    def movieUrl(self) -> str | None:
        movieFile = self.mediaContent.movieFile
        return None if movieFile is None else self._getUrl(
            urlBase=self.URL_MOVIE,
            fileName='movie',
            extension=fileExtension(movieFile)
            )

    @property
    def subtitleUrl(self) -> str | None:
        subtitlesFile = self.mediaContent.subtitlesFile
        return None if subtitlesFile is None else self._getUrl(
            urlBase=self.URL_SUBTITLES,
            fileName='subtitles',
            extension=fileExtension(subtitlesFile)
        )

    @property
    def thumbnailUrl(self) -> str | None:
        thumbnailFile = self.mediaContent.thumbnailFile
        return None if thumbnailFile is None else self._getUrl(
            urlBase=self.URL_THUMBNAIL,
            fileName='thumbnail',
            extension=fileExtension(thumbnailFile)
        )

    def _run(self) -> None:
        self.log.info(f"{self.__class__.__name__} started.")
        try:
            web = cast(bottle.Bottle, self._webApp)

            @web.get(self.URL_MOVIE + '/<name>.<ext>')
            def movie(name: str, ext: str) -> bottle.Response:
                return self._serveFile(self.mediaContent.movieFile)

            @web.get(self.URL_SUBTITLES + '/<name>.<ext>')
            def subtitles(name: str, ext: str) -> bottle.Response:
                return self._serveFile(self.mediaContent.subtitlesFile)

            @web.get(self.URL_THUMBNAIL + '/<name>.<ext>')
            def thumbnail(name: str, ext: str) -> bottle.Response:
                return self._serveFile(self.mediaContent.thumbnailFile)

            web.run(server=self._serverAdapter, quiet=True)

        finally:
            self.log.info(f"{self.__class__.__name__} stopped.")

    def _serveFile(self, filePath: Path | None) -> bottle.Response:
        if filePath is None:
            return bottle.HTTPError(410, 'Resource no longer available.')

        response = bottle.static_file(filename=filePath.name, root=filePath.parent)
        if 'Last-Modified' in response.headers:
            del response.headers['Last-Modified']

        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, HEAD'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

        return response

    def _getUrl(self, urlBase: str, fileName: str, extension: str) -> str:
        host = castNotNull(self._serverAdapter).host
        port = castNotNull(self._serverAdapter).port
        return f"http://{host}:{port}{urlBase}/{fileName}.{extension}"

    @classmethod
    def _getServerAdapter(cls) -> ServerAdapter:
        return ServerAdapter(
            host=cls._resolveHost(),
            port=cls._resolvePort()
        )

    @staticmethod
    def _resolveHost() -> str:
        hostIps = socket.gethostbyname_ex(socket.gethostname())[2]
        hostIps = [ip for ip in hostIps if not ip.startswith("127.")]
        if hostIps:
            return hostIps[0]

        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as sock:
            sock.connect(("8.8.8.8", 53))
            return cast(IpV4Address, sock.getsockname())[0]

    @staticmethod
    def _resolvePort() -> int:
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.bind(('0.0.0.0', 0))
            return cast(IpV4Address, sock.getsockname())[1]
