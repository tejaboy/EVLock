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
	# For this practical, we only use one motor.

	motor = LargeMotor()

def open_safe():
	# When this function is being called, we will move the motor at 100 Power for 1200 ms.
	# There are many other methods avaible such as `on` and `on_for_rotations`.
	# For a list of avaible motor related methods, kindly refer to the following sites:
	#	- https://sites.google.com/site/ev3devpython/learn_ev3_python/using-motors (beginner friendly)
	#	- https://python-ev3dev.readthedocs.io/en/ev3dev-jessie/ ('official' documentation)
	
	motor.on_for_seconds(100, 1.2)

## MQTT
def setupMQTT():
	# We will create an MQTT Client object here and connect it to the free mosquitto server.

    client = mqtt.Client()
    client.connect("test.mosquitto.org", 1883, 60)

	# Here, we defines that when the client is connected to the broker, the function on_connect() shall be called.
	# 						when a message is received, the function on_message() shall be called.

    client.on_connect = on_connect
    client.on_message = on_message

	# This method tell the client object to keep checking for incoming messages.

    client.loop_forever()

def on_connect(client, userdata, flags, rc):
	# When we are connected to the MQTT Broker, we shall subscribe to the channel "ev3dev-safe".
	# For this practical, since everyone will be using the same broker, change it to something unique. eg. "joel-safe".

    debug_print("Connected to MQTT!")

    client.subscribe("ev3dev-safe")

def on_message(client, userdata, msg):
	# Whenever the brocker send a message (payload), this function will be called.
	# Here, we check if the message is equal to "unlock". And if it is, we call the open_safe() function.

    if msg.payload.decode() == "unlock":
        debug_print("Unlocking ...")

        open_safe()

def debug_print(*args, **kwargs):
	'''
	Print debug messages to stderr.
	This shows up in the output panel in VS Code
	'''
	
	print(*args, **kwargs, file=sys.stderr)
	print(*args)

if __name__ == '__main__':
	# Play a beep sound before executing the main function.

	debug_print("Started!")
	Sound.beep()
	main()