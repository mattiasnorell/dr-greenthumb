#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from providers.TemperatureSensor import TemperatureSensor
from scheduledjobs.jobbase import JobBase
#from FanManager import FanManager

class CheckTemperature(JobBase):

    def __init__(self):
        super().__init__()
        self.temperatureSensors = TemperatureSensor()
        #fanManager = FanManager()

    def run(self):
        
        for sensor in self.temperatureSensors.getSensors():
            print("Sensor: ", sensor.name)
            print("Temperature: ", sensor.temperature , "°C (max: ", sensor.max ,"°C)\n")

            self.sqliteDatabase.query("INSERT INTO SensorData (SensorId,Datetime, SensorValue) VALUES(?,datetime('now','localtime'),?)",(sensor.id, sensor.temperature))

            if sensor.temperature > sensor.max:
                self.logger.log("Sensor " + sensor.name + " is above max value\n")
                #fanManager.runFan(30)
                break