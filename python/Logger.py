#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from SqliteDatabase import SqliteDatabase
from Singleton import Singleton

class Logger(metaclass=Singleton):
	
	def __init__(self):
		print("Logger is good to go")
		self.sqliteDatabase = SqliteDatabase()

	def log(self, val):
		print("Logger ::", val)
		self.sqliteDatabase.query ("INSERT INTO Logs (DateTime, Message) VALUES(datetime('now','localtime'),?)",(val,))