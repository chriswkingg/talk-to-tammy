import datetime
import discord
import ai
import google_search
import dictionary
tts_enabled = False

async def input_handler(message):
    global tts_enabled
    author = message.author
    channel = message.channel
    voicechannel = author.voice.channel
    message_string = message.content.lower().replace('$', '') #Removes the $ when sending to message handler
    response = ""
    if message_string.find("whatisthedate") != -1:
        response = datetime.datetime.now().strftime("%B " "%Y")
    elif message_string.find("whatisthetime") != -1:
        response = datetime.datetime.now().strftime("The time is: %I:%M %p")

    elif message_string.find("lookup") != -1:
        quer = message_string.split(' ',1)[1]
        response = dictionary.dict_look_up(quer)

    elif message_string.find("google") != -1:
        quer = message_string.split(' ',1)[1]
        response = google_search.search(quer)
        
    elif message_string.find("join") != -1:
        try:
            response = "Joining VC"
            await voicechannel.connect()
        except discord.errors.ClientException:
            response = "Error: Already connected to a channel"
    elif message_string.find("leave") != -1:
        server=message.guild
        voice_client = server.voice_client
        try: 
            response = "Leaving VC"
            await voice_client.disconnect(force = True)
        except AttributeError:
            response = "Error: Not connected to a voice channel"
    elif message_string.find("tts true") != -1:
        tts_enabled = True
        response = "tts enabled"
    elif message_string.find("tts false") != -1:
        tts_enabled = False
        response = "tts disabled"
    else:
        response = ai.chatBotResponse(message_string)
        response = response if response else "Tammy doesn't know what you said! \nI shat myself"
    
    await message.channel.send(response, tts=tts_enabled)
