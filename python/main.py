#!/usr/bin/python

import schedule
import time
import datetime

from scheduledjobs.checktemperature import CheckTemperature
from scheduledjobs.takephoto import TakePhoto
from scheduledjobs.checkwaterlevel import CheckWaterLevel
from scheduledjobs.checkhumidity import CheckHumidity
from scheduledjobs.checklight import CheckLight

from core.settings import Settings
from core.logger import Logger

print("\nHello, I'm Dr. Greenthumb - version: 0.1")

print("\n_Setting up core_")
settings = Settings() 
logger = Logger()

print("\n_Setting up schedule_")
check_temperature = CheckTemperature()
check_light = CheckLight()
check_waterlevel = CheckWaterLevel()
check_humidity = CheckHumidity()

schedule.every(10).minutes.do(check_temperature.run)
schedule.every(5).seconds.do(check_light.run)
schedule.every(10).seconds.do(check_waterlevel.run)
schedule.every(10).minutes.do(check_humidity.run)

# Things that require a RaspberryPi
if settings.config.enviroment.hostIsRaspberryPi == True:
    take_photo = TakePhoto()
    schedule.every(10).minutes.do(take_photo.run)

print("\nSetup complete!\n")

logger.log("Application started at {}".format(datetime.datetime.now()))

while True:
    schedule.run_pending()
    time.sleep(60)