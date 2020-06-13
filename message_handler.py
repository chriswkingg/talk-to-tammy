import datetime
import discord
import ai
import google_search
import wiki_search
import Dictionary
import translator
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
        response = Dictionary.dict_look_up(quer)

    elif message_string.find("google") != -1:
        quer = message_string.split(' ',1)[1]
        response = google_search.search(quer)

    elif message_string.find("translate") != -1:
        quer = message_string.split(' ',1)[1]
        response = translator.translate(quer)

    elif message_string.find("wiki") != -1:
        quer = message_string.split(' ',2)[2]
        search_type = message_string.split(' ')[1]
        if search_type == 'title':
            response = wiki_search.findTitles(quer)
        elif search_type == 'summary':
            response = wiki_search.articleSummary(quer)
        elif search_type == 'link':
            response = wiki_search.getLink(quer)
        else:
            response = "invalid command, please check my commands"
        
    
    elif message_string.find("what can you do") != -1:
        response = "My commands can be found on my website! "
        
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
        response = response if response else "Tammy doesn't know what you said! \nMy devs are too dumb to teach me more things :("
    
    await message.channel.send(response, tts=tts_enabled)
