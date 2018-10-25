#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from SqliteDatabase import SqliteDatabase
from sensors.temperature import Temperature
import os.path

class TemperatureSensor:
	
	def __init__(self):
		self.sqliteDatabase = SqliteDatabase()

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
		return ""
	
	def getSensors(self):
		return self.readSensors()

	def readSensors(self):
		sensors = []

		self.sqliteDatabase.query("""SELECT * from Sensors where SensorType = 'temp'""","")

		for reading in self.sqliteDatabase.curs.fetchall():
			sensorId = reading[0]
			sensorSerialNumber = str(reading[1])
			sensorName = str(reading[2])
			sensorType = str(reading[3])
			sensorMinValue = reading[4]
			sensorMaxValue = reading[5]
			text = self.getSensorConfigFile(sensorSerialNumber)  

			if text == "":
				print("Sensor not found: ", sensorName, ", S/N:", sensorSerialNumber)
				continue

			temp = self.parseTemperature(text)

			with self.sqliteDatabase.conn:
				if sensorType == "temp":
					sensor = Temperature(sensorId, sensorSerialNumber, sensorName, sensorType, temp, sensorMinValue, sensorMaxValue)
					sensors.append(sensor)

		return sensors
