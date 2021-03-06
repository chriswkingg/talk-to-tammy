#Talk with Tammy created by Chris King, Rohan Singh, Daniel Qiu, and Lauren Rowe

import os 
import discord
import message_handler
import games

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
    message_string = message.content.lower()
    if author == client.user:
        return
    if message_string == "$games":
        await games.init_games(client, message)
    elif message_string[0] == '$' and games.game_enabled == False:
        await message_handler.input_handler(message)
    

client.run(TOKEN)