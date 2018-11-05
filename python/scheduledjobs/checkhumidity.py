#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from scheduledjobs.jobbase import JobBase
from sensors.HumiditySensor import HumiditySensor

class CheckHumidity(JobBase):
    def __init__(self):
        super().__init__()
        self.sensor = HumiditySensor()

    def run(self):
        for sensor in self.sensor.getSensors():
            print("CheckHumidity :: {} Sensor: {}% (max: {}%)".format(sensor.name, sensor.value, sensor.max))

            self.api.post("/sensors/%s/data" % (sensor.id), {'value': sensor.value})
            
            if sensor.value > sensor.max:
                message = "Sensor " + sensor.name + " is above max value"
                self.api.post("log" % (sensor.id), {message: message})
                break