#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from connectors.apiconnector import ApiConnector
from sensors.light import Light
from Logger import Logger

class LightSensor:
	
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

		#GPIO.setmode(GPIO.BCM)
		#GPIO.setwarnings(False)
		#GPIO.setup(17,GPIO.IN)

		for sensor in result['data']:
			sensorId = sensor['Id']
			sensorSerialNumber = sensor['SensorId']
			sensorName = sensor['SensorName']
			sensorType = sensor['SensorType']
			sensorMinValue = sensor['MinValue']
			sensorMaxValue = sensor['MaxValue']
			#value = GPIO.input(17)
			value = 1

			sensor = Light(sensorId, sensorSerialNumber, sensorName, sensorType, value, sensorMinValue, sensorMaxValue)
			sensors.append(sensor)

		return sensors
