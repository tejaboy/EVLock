import paho.mqtt.client as mqtt

def connect():
    # We will create an MQTT Client object here and connect it to the free mosquitto server.

    global client

    client = mqtt.Client()
    client.connect("test.mosquitto.org", 1883, 60)

    print("Connected to MQTT Server!")

def send_unlock():
    # When we receive this command, we send a message to the MQTT broker.
    
    global client

    client.publish("ev3dev-safe", "unlock")

    print("Unlocking Smart Safe!")