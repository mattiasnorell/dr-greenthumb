#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Settings:
	def __init__(self, config):
		self.api = ApiSettings(config["api"])
		self.backup = BackupSettings(config["backup"]) 
		self.enviroment = EnviromentSettings(config["enviroment"]) 

class ApiSettings:
	def __init__(self, config):
		self.basepath = config["basepath"]

class BackupSettings:
	def __init__(self, config):
		self.database = config["database"]
		self.max_database_backups = config["max_database_backups"]

class EnviromentSettings:
	def __init__(self, config):
		self.debug = config["debug"]