#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import sqlite3
from pathlib import Path


class SettingsRepository:

    _TABLE = 'SETTINGS'
    _COL_ID = 'ID'
    _COL_VALUE = 'VALUE'

    def __init__(self, dbPath: Path) -> None:
        self._dbPath: Path = dbPath

        self._createDb()

    def get(self, key: str) -> str | None:
        with self._connect() as db:
            cursor = db.execute(f'SELECT {self._COL_VALUE} FROM {self._TABLE} WHERE {self._COL_ID}=?', (key,))
            row = cursor.fetchone()
            return row[0] if row is not None \
                else None

    def set(self, key: str, value: str) -> None:
        with self._connect() as db:
            db.execute(f'INSERT OR REPLACE INTO {self._TABLE} ({self._COL_ID}, {self._COL_VALUE}) values (?, ?)', (key, value))

    def _createDb(self) -> None:
        with self._connect() as db:
            db.execute(f'''CREATE TABLE IF NOT EXISTS {self._TABLE} (
                {self._COL_ID}    TEXT PRIMARY KEY NOT NULL,
                {self._COL_VALUE} TEXT             NOT NULL
            );''')

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self._dbPath)
