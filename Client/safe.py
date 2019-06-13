#!/usr/bin/env python3

from ev3dev.ev3 import *

import paho.mqtt.client as mqtt
import sys

def main():
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

        # TODO: Motor movement

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