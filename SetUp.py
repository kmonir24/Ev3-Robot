#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
lcd.draw.text((48,13),'Hello, World!')
lcd.update()
sleep(6)
