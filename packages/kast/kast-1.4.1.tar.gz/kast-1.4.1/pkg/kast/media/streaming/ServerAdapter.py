#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J.

import socketserver
import wsgiref.simple_server as wsgi_server
from typing import Any

import bottle

from kast.utils.log.Loggable import Loggable


class _Server(socketserver.ThreadingMixIn, wsgi_server.WSGIServer):
    daemon_threads = True


class _RequestHandler(Loggable, wsgi_server.WSGIRequestHandler):

    def log_error(self, fmt: str, *args: Any) -> None:
        self.log.error(fmt % args)

    def log_message(self, fmt: str, *args: Any) -> None:
        self.log.info(fmt % args)


class ServerAdapter(Loggable, bottle.ServerAdapter):

    def __init__(self, host: str, port: int) -> None:
        super().__init__(host=host, port=port)
        self._server: wsgi_server.WSGIServer | None = None

    def run(self, handler: bottle.Bottle) -> None:
        self._server = wsgi_server.make_server(
            host=self.host,
            port=self.port,
            app=handler,
            server_class=_Server,
            handler_class=_RequestHandler
        )
        self._server.serve_forever()

    def stop(self) -> None:
        server = self._server
        if server is not None:
            server.shutdown()
