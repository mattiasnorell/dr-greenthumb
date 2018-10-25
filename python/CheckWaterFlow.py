#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sqlite3
import os.path
import datetime
import time
from Logger import Logger

conn = sqlite3.connect("/data/websites/greenhouse.local/db/greenhouse.db")
curs=conn.cursor()
logger = Logger(conn)

def readSensors():
	curs.execute ("SELECT * from Sensors where SensorType = 'waterflow'")

	for reading in curs.fetchall():
		sensorId = reading[1]
		sensorName = reading[2]
		sensorMin = reading[4]

		print sensorId
		print sensorName
		print sensorMin

		result = 0.7

		if result < sensorMin:
			logger.log("Water level low")
		
		logger.SaveSensorData(sensorId, sensorName, result)

readSensors()
