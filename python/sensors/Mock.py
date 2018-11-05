#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import datetime

class Mock:

    def __init__(self):
        print("Wiring up", self.__class__.__name__)
        
    def do(self):
        print(datetime.datetime.now().time())