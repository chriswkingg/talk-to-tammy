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

client.run(TOKEN)