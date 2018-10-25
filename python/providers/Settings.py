#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import yaml
from sensors.settings import Settings as SettingsModel
from Singleton import Singleton

class Settings(metaclass=Singleton):
	
	def __init__(self):
		print("Settings loaded")

		content = yaml.load(open("settings.yaml", "r"))
		self.config = SettingsModel(content)