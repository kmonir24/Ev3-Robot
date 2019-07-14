#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

#Left
mb = LargeMotor('outB')

#Right
mc = LargeMotor('outC')

#Sensors
ts = TouchSensor('in2')

ls = LightSensor('in3')

us = UltrasonicSensor('in4')
units = us.units

cl = ColorSensor('in1')
cl.mode = 'COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')

lcd = Screen()
lcd.draw.text((48,13),'Hello, world.')
lcd.update()

distance = us.value()
light = ls.reflected_light_intensity
target = 40

def avoid_object():
    # Leds.set_color(Leds.LEFT, Leds.RED)
    # Leds.set_color(Leds.RIGHT, Leds.RED)
    # mb.run_timed(time_sp=6000, speed_sp=400)
    # mc.run_timed(time_sp=6000, speed_sp=-150)
    # while mb.state == 'running':
    #     time.sleep(5)
    # mb.run_timed(time_sp=6000, speed_sp=-150)
    # mc.run_timed(time_sp=6000, speed_sp=400)
    # while mb.state == 'running':
    #     time.sleep(5)
        mb.run_timed(time_sp = 4000, speep_sp = 400)
        mc.run_timed(time_sp = 4000, speep_sp = 700)
        sleep(3)
        mb.run_timed(time_sp = 4000, speep_sp = 500)
        mc.run_timed(time_sp = 4000, speep_sp = 400)
        sleep(3)
        mb.run_timed(time_sp = 4000, speep_sp = 700)
        mc.run_timed(time_sp = 4000, speep_sp = 400)

while not ts.value():    # Stop program by pressing touch sensor button
    distance = us.value()
    light = ls.reflected_light_intensity

    Leds.set_color(Leds.LEFT, Leds.GREEN)
    Leds.set_color(Leds.RIGHT, Leds.GREEN)
    if light < 40: #Turn Right
        if distance < 200:
            avoid_object()
            sleep(5)
        else:
            mb.run_forever(speed_sp=400)
            mc.run_forever(speed_sp=-150)
    elif light > 60: #Turn Left
        if distance < 200:
            avoid_object()
            sleep(5)
        else:
            mb.run_forever(speed_sp=-100)
            mc.run_forever(speed_sp=350)
    else:
        if distance < 200:
            avoid_object()
            sleep(5)
        else:
            mb.run_forever(speed_sp=350+3*(target-light))
            mc.run_forever(speed_sp=350-3*(target-light))
            print(colors[cl.value()])
    if colors[cl.value()] == 'red':
        Sound.beep()
        break
    if colors[cl.value()] == 'green':
        Sound.beep()

Sound.beep()
Leds.set_color(Leds.LEFT, Leds.GREEN)  #set left led green before exiting
mb.stop()
mc.stop()

# to make extra sure the motors have stopped:
mb.run_forever(speed_sp=0)
mc.run_forever(speed_sp=0)
