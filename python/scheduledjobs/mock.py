#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import datetime

class Mock:

    def __init__(self):
        print("Wiring up", self.__class__.__name__)
        
    def run(self):
        print(self.__class__.__name__, datetime.datetime.now().time())