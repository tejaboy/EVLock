import discord
from discord.ext import commands
import paho.mqtt.client as mqtt
import mqttcontroller

DISCORD_TOKEN = "DISCORD_TOKEN"
UNLOCK_TOKEN = "1234"

bot = commands.Bot(command_prefix = "!")

@bot.command()
async def unlock(context, _unlock_token = None):
    if _unlock_token == UNLOCK_TOKEN:
        await context.send("Correct PIN! Unlocking Smart Safe!")

        mqttcontroller.send_unlock()
    else:
        await context.send("Please enter the correct PIN!")

@bot.event
async def on_ready():
    print("Bot ready!")

mqttcontroller.connect()
bot.run(DISCORD_TOKEN)