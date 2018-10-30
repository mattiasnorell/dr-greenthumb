#!/usr/bin/python

import schedule
import time
import datetime
from providers.Mock import Mock as MockProvider
from scheduledjobs.mock import Mock as MockJob
from scheduledjobs.backupdatabase import BackupDatabase
from scheduledjobs.checktemperature import CheckTemperature
#from scheduledjobs.takephoto import TakePhoto
from scheduledjobs.checkwaterlevel import CheckWaterLevel
from scheduledjobs.checkhumidity import CheckHumidity

from providers.Settings import Settings
from Logger import Logger

print("\nHello, I'm Dr. Greenthumb - version: 0.1")

print("\n_Setting up core_")
settings = Settings() 
logger = Logger()

print("\n_Setting up schedule_")
check_temperature = CheckTemperature()
#backup_database = BackupDatabase()
#take_photo = TakePhoto()
check_waterlevel = CheckWaterLevel()
check_humidity = CheckHumidity()

schedule.every(10).minutes.do(check_temperature.run)
#schedule.every(10).minutes.do(take_photo.run)
#schedule.every().day.do(backup_database.run)
schedule.every(10).seconds.do(check_waterlevel.run)
schedule.every(10).minutes.do(check_humidity.run)

print("\nSetup complete!\n")

logger.log("Application started at {}".format(datetime.datetime.now()))

while True:
    schedule.run_pending()
    time.sleep(10)