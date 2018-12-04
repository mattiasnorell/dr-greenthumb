#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from connectors.apiconnector import ApiConnector
from core.logger import Logger
import RPi.GPIO as GPIO

class Light:
	def __init__(self, id, serialNumber, name, sensorType, value, min, max):
		self.id = id
		self.serialNumber = serialNumber
		self.name = name
		self.type = sensorType
		self.value = value
		self.min = min
		self.max = max

class LightSensor:
	
	gpioPin = 17

	def __init__(self):
		self.api = ApiConnector()
		self.logger = Logger()

	def getSensors(self):
		return self.readSensors()

	def readSensors(self):
		sensors = []

		result = self.api.get("/sensors/type/light")

		if result['status'] != 200:
			return sensors

		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.gpioPin,GPIO.IN)

		for sensor in result['data']:
			sensorId = sensor['Id']
			sensorSerialNumber = sensor['SensorId']
			sensorName = sensor['SensorName']
			sensorType = sensor['SensorType']
			sensorMinValue = sensor['MinValue']
			sensorMaxValue = sensor['MaxValue']
			sensorValue = GPIO.input(self.gpioPin)

			sensor = Light(sensorId, sensorSerialNumber, sensorName, sensorType, sensorValue, sensorMinValue, sensorMaxValue)
			sensors.append(sensor)

		return sensors
