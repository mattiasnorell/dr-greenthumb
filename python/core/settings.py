#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import yaml
from core.models.settings import Settings as SettingsModel
from core.singleton import Singleton

class Settings(metaclass=Singleton):
	
	def __init__(self):
		print("Settings loaded")

		content = yaml.load(open("settings.yaml", "r"))
		self.config = SettingsModel(content)