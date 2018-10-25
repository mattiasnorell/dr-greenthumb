#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Settings:
	def __init__(self, config):
		self.database = DatabaseSettings(config["database"])
		self.backup = BackupSettings(config["backup"]) 
		self.enviroment = EnviromentSettings(config["enviroment"]) 

class DatabaseSettings:
	def __init__(self, config):
		self.path = config["path"]

class BackupSettings:
	def __init__(self, config):
		self.database = config["database"]
		self.max_database_backups = config["max_database_backups"]

class EnviromentSettings:
	def __init__(self, config):
		self.debug = config["debug"]