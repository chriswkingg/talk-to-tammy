
import os 
import discord
import datetime


from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.find("$whatisthedate") != -1:
        await message.channel.send(datetime.datetime.now())


client.run(TOKEN)

channel = discord.TextChannel()






