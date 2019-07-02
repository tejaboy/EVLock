import discord
from discord.ext import commands

import paho.mqtt.client as mqtt
import mqttcontroller

# Discord Bot Token/Key
DISCORD_TOKEN = "DISCORD_TOKEN" 
# Password to use when commanding the Discord bot to unlock safe
UNLOCK_TOKEN = "1234"

# We create a new discord commands bot and
# specify that our commands starts with "!".
bot = commands.Bot(command_prefix = "!")
# Create a MQTT client for all MQTT communication
mqtt_client = mqtt.Client()


@bot.command()
async def unlock(context, unlock_token=None):
    """Attempts to unlock the safe with the given unlock token.
    Example usage: "!unlock 1234"

    This function will check if the first parameter, unlock_token, is the same
    as our predefined UNLOCK_TOKEN constant. If it is, it will tell the
    mqttcontroller to send an unlock message to the MQTT broker.
    """

    if unlock_token == UNLOCK_TOKEN:
        await context.send("Correct PIN! Unlocking Smart Safe!")

        mqttcontroller.send_unlock(mqtt_client)
    else:
        await context.send("Please enter the correct PIN!")


@bot.event
async def on_ready():
    # When the Discord bot is 'ready', we print out that it is ready.
    # Practically, you would prepare logging tools or other hooks here.

    print("Bot ready!")

# Connect the MQTT client to the MQTT broker using mqttcontroller
mqttcontroller.connect(client)

# We enable to Bot over here with the correct DISCORD_TOKEN.
bot.run(DISCORD_TOKEN)
