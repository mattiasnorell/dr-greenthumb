#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Settings:
	def __init__(self, config):
		self.api = ApiSettings(config["api"])
		self.enviroment = EnviromentSettings(config["enviroment"]) 

class ApiSettings:
	def __init__(self, config):
		self.basepath = config["basepath"]

class EnviromentSettings:
	def __init__(self, config):
		self.debug = config["debug"]
		self.hostIsRaspberryPi = False
		
		try:
  			import RPi.GPIO as gpio
  			self.hostIsRaspberryPi = True
		except (ImportError, RuntimeError):
  			self.hostIsRaspberryPi = False