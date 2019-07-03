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
    # We will do all initialization of motors and sensors here.
    # For this practical, we only be using one motor.

    motor = LargeMotor()

def open_safe():
    # When this function is called, we will move the motor at 100 Power for
    # 1200 ms.
    # There are many other ways to move the motor such as `on` and
    # `on_for_rotations`.
    # For a list of other available motor related methods, refer to the
    # following sites:
    #    - https://sites.google.com/site/ev3devpython/learn_ev3_python/using-motors (beginner friendly)
    #    - https://python-ev3dev.readthedocs.io/en/ev3dev-jessie/ ('official' documentation)

    motor.on_for_seconds(100, 1.2)

## MQTT
def setupMQTT():
    # We will create an MQTT Client object here and connect it to the free
    # mosquitto server.

    client = mqtt.Client(transport="websockets")
    client.connect("test.mosquitto.org", 8080, 60)

    # Here, we defines that:
    # When the client is connected to the broker, call on_connect()
    # When a message is received, call on_message()

    client.on_connect = on_connect
    client.on_message = on_message

    # This method tells the client object to keep checking
    # for incoming messages.
    client.loop_forever()

def on_connect(client, userdata, flags, rc):
    # When we are connected to the MQTT Broker, we shall subscribe to the
    # "ev3dev-safe" channel.
    # For this practical, since everyone will be using the same broker,
    # change it to something unique. eg. "joel-safe".

    debug_print("Connected to MQTT!")

    client.subscribe("ev3dev-safe")

def on_message(client, userdata, msg):
    # Whenever the broker sends a message (payload),
    # this function will be called.

    # Here, we check if the message is equal to "unlock".
    # If it is, we call the open_safe() function.
    if msg.payload.decode() == "unlock":
        debug_print("Unlocking ...")
        open_safe()

def debug_print(*args, **kwargs):
    """Print debug messages to stderr.
    This shows up in the output panel in VS Code
    """

    print(*args, **kwargs, file=sys.stderr)
    print(*args)

if __name__ == '__main__':
    debug_print("Started!")

    # Play a beep sound before executing the main function.
    Sound.beep()
    main()