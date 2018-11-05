#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from DistanceSensorValue import DistanceSensorValue

import RPi.GPIO as GPIO
import os.path
import time

class DistanceSensor:

    GPIO_TRIGGER = 4
    GPIO_ECHO    = 22

    def __init__(self):
        print("Distance sensor init")

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        GPIO.output(self.GPIO_TRIGGER, False)

    def getSensorValue(self):

        numberOfPings = 10
        pingInterval = 1
        result = 0

        time.sleep(2)
        print(self.GPIO_TRIGGER, self.GPIO_ECHO)
        for num in range(0, numberOfPings):
            print ("Ping " + str(num + 1))

            GPIO.output(self.GPIO_TRIGGER, True)
            time.sleep(0.00001)
            GPIO.output(self.GPIO_TRIGGER, False)
            start = time.time()

            while GPIO.input(self.GPIO_ECHO)==0:
                print(0)
                start = time.time()

            while GPIO.input(self.GPIO_ECHO)==1:
                print(1)
                stop = time.time()

            elapsed = stop-start

            distance = (elapsed * 34300) / 2
            
            result = result + float(distance)

            time.sleep(pingInterval)


        endResult = result / numberOfPings
        
        print ("Result: " + str(endResult))

        #GPIO.cleanup()

        return DistanceSensorValue(endResult)