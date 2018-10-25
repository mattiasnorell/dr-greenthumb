#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from scheduledjobs.jobbase import JobBase
from providers.HumiditySensor import HumiditySensor

class CheckHumidity(JobBase):
    def __init__(self):
        super().__init__()
        self.sensor = HumiditySensor()

    def run(self):
        for sensor in self.sensor.getSensors():
            print "Sensor: ", sensor.name
            print "Humidity: ", sensor.value , "°C (max: ", sensor.max ,"°C)\n"

            self.sqliteDatabase.query ("INSERT INTO SensorData (SensorId, Datetime, SensorValue) VALUES(?,datetime('now','localtime'),?)",(sensorId, value))

            if sensor.value > sensor.max:
                self.logger.log("Sensor " + sensor.name + " is above max value\n")
                break