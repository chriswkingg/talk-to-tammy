import ai
import datetime


def input_handler(message):
    if message.find("whatisthedate") != -1:
        return datetime.datetime.now().strftime("%B " "%Y")
    else:
        response = ai.chatBotResponse(message)
        return response if response else "I just shat myself" //If the AI doesnt reply 
    