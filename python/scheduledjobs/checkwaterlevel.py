#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import os.path
import datetime
import time
from Logger import Logger
from SqliteDatabase import SqliteDatabase

class CheckWaterLevel:
	
	def __init__(self):
		
		print("Wiring up", self.__class__.__name__)

		self.GPIO_TRIGGER = 22
		self.GPIO_ECHO    = 24

		GPIO.setmode(GPIO.BCM)
		
		GPIO.setup(self.GPIO_TRIGGER,GPIO.OUT)
		GPIO.setup(self.GPIO_ECHO,GPIO.IN)
		GPIO.output(self.GPIO_TRIGGER, False)

		self.logger = Logger()
		self.sqliteDatabase = SqliteDatabase()

		time.sleep(0.5)

	def run(self):
		self.sqliteDatabase.query ("SELECT * from Sensors where SensorType = 'waterlevel'","")

		for reading in self.sqliteDatabase.curs.fetchall():
			sensorId = reading[1]
			sensorName = reading[2]
			sensorMin = reading[4]
			sensorMax = reading[5]

			numberOfPings = 10
			pingInterval = 1
			result = 0

			for num in range(0, numberOfPings):
				print("Ping " + str(num + 1))

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


			if result < sensorMin:
				self.logger.log("Water level low")
			
			
			endResult = result / numberOfPings

			if result < sensorMin:
				self.logger.log("Water level low")
			
			print("Result: " + str(endResult))
			print((sensorMin/endResult) *100)

			self.sqliteDatabase.query("INSERT INTO SensorData (SensorId,Datetime, SensorValue) VALUES(?,datetime('now','localtime'),?)",(sensorId, (sensorMin / endResult) - 1))

