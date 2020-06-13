import datetime
import discord
import ai
import games

async def input_handler(message):
    author = message.author
    channel = message.channel
    voicechannel = author.voice.channel
    message_string = message.content.lower().replace('$', '') #Removes the $ when sending to message handler

    if message_string.find("whatisthedate") != -1:
        await message.channel.send(datetime.datetime.now().strftime("%B " "%Y"))
    elif message_string.find("hi") != -1:
        await message.channel.send("Hi " + author.name)
    elif message_string.find("whatisthetime") != -1:
        await message.channel.send(datetime.datetime.now().strftime("The time is: %I:%M %p"))
    elif message_string.find("games") != -1:
        await games.playGame(message)
    elif message_string.find("join") != -1:
        try:
            await message.channel.send("Joining VC")
            await voicechannel.connect()
        except discord.errors.ClientException:
            await message.channel.send("Error: Already connected to a channel")
    elif message_string.find("leave") != -1:
        server=message.guild
        voice_client = server.voice_client
        try: 
            await message.channel.send("Leaving VC")
            await voice_client.disconnect(force = True)
        except AttributeError:
            await message.channel.send("Error: Not connected to a voice channel")
    else:
        response = ai.chatBotResponse(message_string)
        await message.channel.send(response if response else "Tammy doesn't know what you said! \n My devs are too dumb to teach me more things :(")