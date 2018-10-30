#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from sensors.humidity import Humidity
import os.path
#import Adafruit_DHT
from connectors.apiconnector import ApiConnector

class HumiditySensor:
	
	def __init__(self):
		self.api = ApiConnector()

	def getSensorValue(self, serialNumber):
		#sensorType = Adafruit_DHT.DHT22
		#humidity, temperature = Adafruit_DHT.read_retry(sensorType, serialNumber)
		humidity = 10
		return humidity

	def getSensors(self):
		return self.readSensors()

	def readSensors(self):
		returnValue = []

		result = self.api.get("/sensors/type/humidity")

		if result['status'] != 200:
			return returnValue

		for sensor in result['data']:
			sensorId = sensor['Id']
			sensorSerialNumber = sensor['SensorId']
			sensorName = sensor['SensorName']
			sensorType = sensor['SensorType']
			sensorMinValue = sensor['MinValue']
			sensorMaxValue = sensor['MaxValue']

			value = self.getSensorValue(sensorSerialNumber)

			sensor = Humidity(sensorId, sensorSerialNumber, sensorName, sensorType, value, sensorMinValue, sensorMaxValue)
			returnValue.append(sensor)

		return returnValue
