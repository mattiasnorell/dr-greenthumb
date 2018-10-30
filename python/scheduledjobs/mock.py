#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import datetime
from scheduledjobs.jobbase import JobBase

class Mock(JobBase):

    def __init__(self):
        super().__init__()
        
    def run(self):
        print(self.__class__.__name__, datetime.datetime.now().time())
        results = self.apiConnector.get("/sensors/type/temp")
        for reading in results:
            print(reading['SensorName'])