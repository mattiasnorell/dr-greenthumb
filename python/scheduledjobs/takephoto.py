#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import datetime
from CameraManager import CameraManager

class TakePhoto:

    def __init__(self):
        print("Wiring up", self.__class__.__name__)
        self.cameraManager = CameraManager()
        
    def run(self):
        self.cameraManager.TakePhoto()