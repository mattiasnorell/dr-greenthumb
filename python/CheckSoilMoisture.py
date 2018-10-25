#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sqlite3
import os.path
from MoistureSensorProvider import MoistureSensorProvider
from Logger import Logger
import RPi.GPIO as GPIO
import time

conn = sqlite3.connect("/data/websites/greenhouse.local/db/greenhouse.db")
curs=conn.cursor()

sensors = MoistureSensorProvider(conn)
logger = Logger(conn)

def saveValue(sensorId, value):
    print sensorId
    print value

    curs.execute ("INSERT INTO SensorData (SensorId, Datetime, SensorValue) VALUES(?,datetime('now','localtime'),?)",(sensorId, value))
    conn.commit()

def readSensors():
    
    for sensor in sensors.getSensors():
        print "Sensor: ", sensor.name
        print "Moisture: ", sensor.value , "(min: ", sensor.min ,")\n"
        
        saveValue(sensor.id, sensor.value)

        if sensor.value == sensor.min:
            logger.log("Sensor " + sensor.name + " is below min value\n")
            break
        
readSensors()
conn.close()
