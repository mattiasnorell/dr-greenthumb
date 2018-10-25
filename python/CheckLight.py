#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import RPi.GPIO as GPIO
import sqlite3
import os.path
import datetime
import time

conn = sqlite3.connect("/data/websites/greenhouse.local/db/greenhouse.db")
curs=conn.cursor()

def saveValue(sensorId, val):
    print " - Saving value for", sensorId, ": ", val

    curs.execute ("INSERT INTO SensorData (SensorId,Datetime, SensorValue) VALUES(?,datetime('now','localtime'),?)",(sensorId, val))
    conn.commit()

def getStatus(sensorId):
    curs.execute("SELECT * FROM SensorData WHERE SensorId = '" + sensorId + "' ORDER BY DateTime DESC LIMIT 1")
    for reading in curs.fetchall():
#       print reading[1]
#       print reading[2]
#       print reading[3]
        return reading[3]

def currentTimeWithinRange():
	minTime = datetime.time(8)
	maxTime = datetime.time(22)
	currentTime = datetime.datetime.now().time()

	if currentTime >= minTime and currentTime <= maxTime:
		return True

	return False

def readSensors():
    curs.execute ("SELECT * from Sensors where SensorType = 'light'")

    for reading in curs.fetchall():
        print "Sensor found: ", reading[2]

        sensorId = reading[1]

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(17,GPIO.IN)
        GPIO.setup(18, GPIO.OUT)

        currentValue = getStatus(sensorId)

        print "Current value", currentValue
        print "Current sensor value", GPIO.input(17)
#	GPIO.output(18, GPIO.LOW)
#	time.sleep(2)
        if(currentTimeWithinRange() == False and currentValue == 1):
            print " - Out of range, turn lights off"
            GPIO.output(18, GPIO.LOW)
            saveValue(sensorId, 0)
        elif(GPIO.input(17) == 1 and currentValue == 0 and currentTimeWithinRange() == True):
            print " - Turn lights on"
            GPIO.output(18, GPIO.HIGH)
            saveValue(sensorId, 1)

        elif(GPIO.input(17) == 0 and currentValue == 1 and currentTimeWithinRange() == True):
            print " - Turn lights off"
            GPIO.output(18, GPIO.LOW)
            saveValue(sensorId, 0)

readSensors()
