import paho.mqtt.client as mqtt

def connect():
    global client

    client = mqtt.Client()
    client.connect("test.mosquitto.org", 1883, 60)

    print("Connected to MQTT Server!")

def send_unlock():
    global client

    client.publish("ev3dev-safe", "unlock")

    print("Unlocking Smart Safe!")