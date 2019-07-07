#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

#Left
mb = LargeMotor('outB')

#Right
mc = LargeMotor('outC')

#Sensors
ts = TouchSensor('in2')

cl = ColorSensor('in3')
cl.mode = 'COL-REFLECT'

us = UltrasonicSensor('in4')
units = us.units

lcd = Screen()
lcd.draw.text((48,13),'Hello, world.')
lcd.update()

while not ts.value():    # Stop program by pressing touch sensor button
    distance = us.value()
    color = cl.reflected_light_intensity
    if color < 30: #Turn Right
        mb.run_forever(speed_sp=400)
        mc.run_forever(speed_sp=-150)
    elif color > 70: #Turn Left
        mb.run_forever(speed_sp=-150)
        mc.run_forever(speed_sp=400)
        print(color)
    else:
        mb.run_forever(speed_sp=300+3*(50-color))
        mc.run_forever(speed_sp=300-3*(50-color))
        print(color)
    if distance < 100:
    	Leds.set_color(Leds.LEFT, Leds.RED)
        mb.stop(stop_action="hold")
        mc.stop(stop_action="hold")
        break
    else:
        Leds.set_color(Leds.LEFT, Leds.GREEN)
    print(color)

Sound.beep()
Leds.set_color(Leds.LEFT, Leds.GREEN)  #set left led green before exiting
mb.stop(stop_action="hold")
mc.stop(stop_action="hold")
sleep(5000)