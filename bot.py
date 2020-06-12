#Talk with Tammy created by Chris King, Rohan Singh, Daniel Qiu, and Lauren Rowe

import os 
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # Sets vars for convience
    author = message.author
    channel = message.channel
    server = channel.server
    message_string = message.content.lower()
    if author == client.user:
        # Don't let the bot talk to itself... it might become self-aware.
        return
    elif message_string.find("$hi") != -1:
        await message.channel.send("Hi")


client.run(TOKEN)

channel = discord.TextChannel()
