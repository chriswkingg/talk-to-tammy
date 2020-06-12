import datetime
import discord


async def input_handler(message):
    author = message.author
    channel = message.channel
    voicechannel = author.voice.channel
    message_string = message.content.lower().replace('$', '') #Removes the $ when sending to message handler
    if message_string.find("whatisthedate") != -1:
        await message.channel.send(datetime.datetime.now().strftime("%B " "%Y"))

    elif message_string.find("hi") != -1:
        await message.channel.send("Hi")
    elif message_string.find("join") != -1:
        await message.channel.send("Joining VC")
        await voicechannel.connect()
    elif message_string.find("leave") != -1:
        server=message.guild
        voice_client = server.voice_client
        await message.channel.send("Leaving VC")
        await voice_client.disconnect(force = True)




