#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from sensors.humidity import Humidity
import os.path
import Adafruit_DHT
from connectors.apiconnector import ApiConnector

class HumiditySensor:
	
	def __init__(self):
		self.api = ApiConnector()

	def getSensorValue(self, serialNumber):
		sensorType = Adafruit_DHT.DHT22
		humidity, temperature = Adafruit_DHT.read_retry(sensorType, serialNumber)

		return humidity

	def getSensors(self):
		return self.readSensors()

	def readSensors(self):
		sensors = []

		sensors = self.api.get("/sensors/type/humidity")

		for sensor in sensors:
			print(sensor)
		#	sensorId = reading[0]
		#	sensorSerialNumber = str(reading[1])
		#	sensorName = str(reading[2])
		#	sensorType = str(reading[3])
		#	sensorMinValue = reading[4]
		#	sensorMaxValue = reading[5]

		#	value = self.getSensorValue(sensorSerialNumber)

		#	with self.sqliteDatabase.conn:
		#		if sensorType == "humidity":
		#			sensor = Humidity(sensorId, sensorSerialNumber, sensorName, sensorType, value, sensorMinValue, sensorMaxValue)
		#			sensors.append(sensor)

		return sensors
