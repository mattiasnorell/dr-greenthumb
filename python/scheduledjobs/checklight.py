#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from providers.LightSensor import LightSensor
from scheduledjobs.jobbase import JobBase
#from FanManager import FanManager
import datetime

class CheckLight(JobBase):

    def __init__(self):
        super().__init__()
        self.temperatureSensors = LightSensor()
        #fanManager = FanManager()

    def currentTimeWithinRange(self, sensor):
        minTime = datetime.time(sensor.min)
        maxTime = datetime.time(sensor.max)
        currentTime = datetime.datetime.now().time()

        if currentTime >= minTime and currentTime <= maxTime:
            return True

        return False

    def run(self):
        
        sensors = self.temperatureSensors.getSensors()
        for sensor in sensors:

            self.api.post("/sensors/%s/data" % (sensor.id), {'value': sensor.value})

            isWithinRange = self.currentTimeWithinRange(sensor)

            if(isWithinRange == False and sensor.value == 1):
                message = "Sensor {} not within timespan and lights are on, turning lights off".format(sensor.name)
                self.logger.log(message)

                #GPIO.output(18, GPIO.LOW)

            elif(isWithinRange == True and sensor.value == 0):
                message = "Sensor {} within timespan and lights are off, turning lights on".format(sensor.name)
                self.logger.log(message)

                #GPIO.output(18, GPIO.HIGH)