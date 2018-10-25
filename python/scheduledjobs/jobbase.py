#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from Logger import Logger
from SqliteDatabase import SqliteDatabase

class JobBase:
        def __init__(self):
                print("Wiring", self.__class__.__name__)
                self.sqliteDatabase = SqliteDatabase()
                self.logger = Logger()
