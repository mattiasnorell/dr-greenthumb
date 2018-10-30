#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from Logger import Logger
import RPi.GPIO as GPIO
import time

class FanManager:
	
	def __init__(self):
		self.logger = Logger()

	def runFan(self, runtime = 60):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(18,GPIO.OUT)
			
		self.logger.log("Starting fan, running for " + str(runtime) + " seconds")
		GPIO.output(18, GPIO.HIGH)
		time.sleep(runtime)
		self.logger.log("Stopping fan")
		GPIO.output(18, GPIO.LOW)