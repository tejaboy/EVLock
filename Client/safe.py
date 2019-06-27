#!/usr/bin/env python3

from ev3dev.ev3 import *
from ev3dev2.motor import *

import paho.mqtt.client as mqtt
import sys

def main():
    setupMQTT()
    setupEV3()

## EV3
def setupEV3():
	# We will do all the initialization of motors and sensor here.
	# For this practical, there are only one motor.
	motor = LargeMotor()

def open_safe():
	motor.on_for_seconds(100, 1.2)

## MQTT
def setupMQTT():
    client = mqtt.Client()
    client.connect("test.mosquitto.org", 1883, 60)

    client.on_connect = on_connect
    client.on_message = on_message

    client.loop_forever()

def on_connect(client, userdata, flags, rc):
    debug_print("Connected to MQTT!")

    client.subscribe("ev3dev-safe")

def on_message(client, userdata, msg):
    if msg.payload.decode() == "unlock":
        debug_print("Unlocking ...")

        open_safe()

def debug_print(*args, **kwargs):
	'''Print debug messages to stderr.
	This shows up in the output panel in VS Code.pp0
	'''
	
	print(*args, **kwargs, file=sys.stderr)
	print(*args)

if __name__ == '__main__':
	debug_print("Started!")
	Sound.beep()
	main()