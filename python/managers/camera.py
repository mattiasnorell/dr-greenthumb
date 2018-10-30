#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import time
#import picamera
from time import sleep
import datetime
import sqlite3
import os.path
import sys
from core.settings import Settings

class CameraManager:
	
	def __init__(self):
		self.settings = Settings()

	def takePicture(self):
		#camera = picamera.PiCamera()
		#camera.resolution = (1024, 768)
		#camera.rotation = 180
		#camera.annotate_background = picamera.Color('black')
		#camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		#camera.capture(self.settings.camera.path, resize=(940, 705))
		print("Mock photo")