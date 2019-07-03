import paho.mqtt.client as mqtt


def connect(client):
    # Connect the client to the free mosquitto server
    client.connect("test.mosquitto.org", 8080, 60)

    print("Connected to MQTT Server!")


def send_unlock(client):
    # Send a message to the MQTT broker.
    client.publish("ev3dev-safe", "unlock")

    print("Unlocking Smart Safe!")
