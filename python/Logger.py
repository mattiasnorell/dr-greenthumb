#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from core.singleton import Singleton
from connectors.apiconnector import ApiConnector

class Logger(metaclass=Singleton):
	
	def __init__(self):
		self.api = ApiConnector()
		print("Logger is good to go")

	def log(self, val):
		print("Logger ::", val)
		self.api.post("/log", {'message': val})