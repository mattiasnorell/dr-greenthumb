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
        
        sensors = self.temperatureSensors.getSensors()
        for sensor in sensors:
            print("Sensor: ", sensor.name)
            print("Temperature: ", sensor.value , "°C (max: ", sensor.max ,"°C)\n")

            self.api.post("/sensors/%s/data" % (sensor.id), {'value': sensor.value})

            if sensor.value > sensor.max:
                message = "Sensor {} is above max value".format(sensor.name)
                self.logger.log(message)
                #fanManager.runFan(30)
                break