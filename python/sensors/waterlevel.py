#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Waterlevel:
	def __init__(self, id, serialNumber, name, type, value, min, max):
		self.id = id
		self.serialNumber = serialNumber
		self.name = name
		self.type = type
		self.value = value
		self.min = min
		self.max = max