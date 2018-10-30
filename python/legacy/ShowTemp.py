#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Adafruit_CharLCD as LCD
import time
import syslog
import traceback
from datetime import datetime

lcd_rs        = 21
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

lcd_columns = 16
lcd_rows    = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                                        lcd_columns, lcd_rows, lcd_backlight)


def parseTemperature( input ):
    secondline = input.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    return round(temperature / 1000,1)

def getSensorConfigFile (sensorId):
    sensorPath = "/sys/bus/w1/devices/"+ sensorId  +"/w1_slave"
    tfile = open(sensorPath)
    text = tfile.read()
    tfile.close()
    return text

def updateDisplay (rowOne, rowTwo):
    lcd.clear()
    lcd.message('Inside:  %s%sC\n' % ( rowOne, chr(223) ) )
    lcd.message('Outside: %s%sC' % ( rowTwo, chr(223) ) )

def readSensors():
    sensorSerialNumberOne = "28-000004d48aef"
    configOne = getSensorConfigFile(sensorSerialNumberOne)
    tempOne = parseTemperature(configOne)
    sensorSerialNumberTwo = "28-0000053b4dec"
    configTwo = getSensorConfigFile(sensorSerialNumberTwo)
    tempTwo = parseTemperature(configTwo)
    
    updateDisplay(tempOne, tempTwo)

    time.sleep(3)
    readSensors()

def main():
    readSensors()

if __name__ == '__main__':
    try:
        main()
    except:
        print traceback.format_exc()
