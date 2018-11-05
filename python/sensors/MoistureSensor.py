#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os.path
import RPi.GPIO as GPIO

class MoistureSensor():
	def __init__(self, id, serialNumber, name, type, value, min, max):
		self.id = id
		self.serialNumber = serialNumber
		self.name = name
		self.type = type
		self.value = value
		self.min = min
		self.max = max

class MoistureSensor:
	
	def __init__(self, connection):
		self.api = apiconnector

	def getSensorValue(self, serialNumber):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(serialNumber, GPIO.IN)
		return GPIO.input(serialNumber)

	def getSensors(self):
		return self.readSensors()

	def readSensors(self):
		sensors = []

		sensors = self.api.get("/sensors/type/moisture")

		for reading in sensors:
			sensorId = reading[0]
			sensorSerialNumber = int(reading[1])
			sensorName = str(reading[2])
			sensorType = str(reading[3])
			sensorMinValue = reading[4]
			sensorMaxValue = reading[5]
			value = self.getSensorValue(sensorSerialNumber)  

		#	with self.connection:
		#		if sensorType == "moisture":
		#			sensor = Moisture(sensorId, sensorSerialNumber, sensorName, sensorType, value, sensorMinValue, sensorMaxValue)
		#			sensors.append(sensor)

		return sensors
