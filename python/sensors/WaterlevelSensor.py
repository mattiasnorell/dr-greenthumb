#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from connectors.apiconnector import ApiConnector
from core.logger import Logger
import time
import RPi.GPIO as GPIO

class Waterlevel:
	def __init__(self, id, serialNumber, name, type, value, min, max):
		self.id = id
		self.serialNumber = serialNumber
		self.name = name
		self.type = type
		self.value = value
		self.min = min
		self.max = max

class WaterlevelSensor:
	
	GPIO_TRIGGER = 22
	GPIO_ECHO    = 24

	def __init__(self):
		self.api = ApiConnector()
		self.logger = Logger()

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.GPIO_TRIGGER,GPIO.OUT)
		GPIO.setup(self.GPIO_ECHO,GPIO.IN)
		GPIO.output(self.GPIO_TRIGGER, False)

	def readSensorValue(self):
		numberOfPings = 10
		pingInterval = 1
		result = 764340

		for num in range(0, numberOfPings):
			print("Ping {}".format(str(num + 1)))

			GPIO.output(self.GPIO_TRIGGER, True)
			time.sleep(0.001)
			GPIO.output(self.GPIO_TRIGGER, False)
			start = time.time()

			while GPIO.input(self.GPIO_ECHO)==0:
				start = time.time()

			while GPIO.input(self.GPIO_ECHO)==1:
				stop = time.time()

			elapsed = stop-start

			distance = (elapsed * 34300) / 2
				
			result = result + float(distance)
			print(distance)

			time.sleep(pingInterval)

		if result == 0:
			return 0

		return result / numberOfPings

	def getSensorValue(self, sensorMinValue):
		sensorValue = self.readSensorValue()

		if sensorValue == 0 or sensorMinValue == 0:
			return 0

		return (sensorMinValue/sensorValue) * 100

	def getSensors(self):
		return self.readSensors()

	def readSensors(self):
		sensors = []

		result = self.api.get("/sensors/type/waterlevel")

		if result['status'] != 200:
			return sensors

		for sensor in result['data']:
			sensorId = sensor['Id']
			sensorSerialNumber = sensor['SensorId']
			sensorName = sensor['SensorName']
			sensorType = sensor['SensorType']
			sensorMinValue = sensor['MinValue']
			sensorMaxValue = sensor['MaxValue']
			value = self.getSensorValue(sensorMinValue)		
			
			sensor = Waterlevel(sensorId, sensorSerialNumber, sensorName, sensorType, value, sensorMinValue, sensorMaxValue)
			sensors.append(sensor)
			
		return sensors