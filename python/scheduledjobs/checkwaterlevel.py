#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scheduledjobs.jobbase import JobBase
from providers.WaterlevelSensor import WaterlevelSensor

class CheckWaterLevel(JobBase):
	
	def __init__(self):
		super().__init__()
		self.waterlevelProvider = WaterlevelSensor()


	def run(self):
		
		for sensor in self.waterlevelProvider.getSensors():
			self.api.post("/sensors/{}/data".format(sensor.id),{'value': sensor.value })

			if sensor.value < sensor.min:
				self.logger.log("Water level low")
			
