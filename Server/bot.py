import discord
from discord.ext import commands
import paho.mqtt.client as mqtt
import mqttcontroller

DISCORD_TOKEN = "DISCORD_TOKEN" # Discord Bot Token/Key
UNLOCK_TOKEN = "1234" # Password to use when commanding the Discord bot to unlock safe

# We create a new discord commands bot and specify that our commands starts with "!".
bot = commands.Bot(command_prefix = "!")
# Create a MQTT client for all MQTT communication
mqtt_client = mqtt.Client()


@bot.command()
async def unlock(context, _unlock_token = None):
    # We will check if the first parameter - _unlock_token - is the same as our defined UNLOCK_TOKEN constant.
    # If it is, we will tell mqttcontroller to send the unlock message to the MQTT broker.
    # Example usage: "!unlock 1234".

    if _unlock_token == UNLOCK_TOKEN:
        await context.send("Correct PIN! Unlocking Smart Safe!")

        mqttcontroller.send_unlock(mqtt_client)
    else:
        await context.send("Please enter the correct PIN!")

@bot.event
async def on_ready():
    # When the Discord bot is 'ready', we print out that it is sccessfully connected to the Discord server.
    # In practical, you may want to do reset variables here.

    print("Bot ready!")

# Here, we tell the external script, mqttcontroller to connect to the MQTT broker.
mqttcontroller.connect(client)

# We enable to Bot over here with the correct DISCORD_TOKEN.
bot.run(DISCORD_TOKEN)