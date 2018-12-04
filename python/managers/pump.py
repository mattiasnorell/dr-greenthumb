#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from Logger import Logger
import RPi.GPIO as GPIO
import time

class PumpManager:
	
	gpioPin = 18

	def __init__(self):
		self.logger = Logger()

	def run(self, runtime = 60):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.gpioPin,GPIO.OUT)
			
		self.logger.log("Starting pump, running for " + str(runtime) + " seconds")
		GPIO.output(self.gpioPin, GPIO.HIGH)
		
		time.sleep(runtime)

		self.logger.log("Stopping pump")
		GPIO.output(self.gpioPin, GPIO.LOW)