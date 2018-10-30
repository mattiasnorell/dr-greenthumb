#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from connectors.apiconnector import ApiConnector
from sensors.temperature import Temperature
import os.path
from Logger import Logger

class TemperatureSensor:
	
	def __init__(self):
		self.api = ApiConnector()
		self.logger = Logger()

	def parseTemperature(self, input):
		secondline = input.split("\n")[1]
		temperaturedata = secondline.split(" ")[9]
		temperature = float(temperaturedata[2:])
		return temperature / 1000   

	def getSensorConfigFile (self, sensorId):
		sensorPath = "/sys/bus/w1/devices/"+ sensorId +"/w1_slave"
		if os.path.isfile(sensorPath): 
			tfile = open(sensorPath)
			text = tfile.read()
			tfile.close()
			return text

		return None
	
	def getSensors(self):
		return self.readSensors()

	def readSensors(self):
		sensors = []

		result = self.api.get("/sensors/type/temp")

		if result['status'] != 200:
			return sensors

		for sensor in result['data']:
			sensorId = sensor['Id']
			sensorSerialNumber = sensor['SensorId']
			sensorName = sensor['SensorName']
			sensorType = sensor['SensorType']
			sensorMinValue = sensor['MinValue']
			sensorMaxValue = sensor['MaxValue']
			sensorConfiguration = self.getSensorConfigFile(sensorSerialNumber)  

			if sensorConfiguration == None:
				message = "Sensor not found: {}, S/N: {}".format(sensorName, sensorSerialNumber)
				self.logger.log(message)
				continue

			temp = self.parseTemperature(sensorConfiguration)
			sensor = Temperature(sensorId, sensorSerialNumber, sensorName, sensorType, temp, sensorMinValue, sensorMaxValue)
			sensors.append(sensor)

		return sensors
