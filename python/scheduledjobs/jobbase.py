#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from core.logger import Logger
from connectors.apiconnector import ApiConnector

class JobBase:
        def __init__(self):
                print("Wiring", self.__class__.__name__)
                self.api = ApiConnector()
                self.logger = Logger()
