import ai
import datetime


def input_handler(message):
    if message.find("whatisthedate") != -1:
<<<<<<< Updated upstream
        return datetime.datetime.now().strftime("%B " "%Y")
    else:
        response = ai.chatBotResponse(message)
        return response if response else "I just shat myself" //If the AI doesnt reply 
    
=======
        return datetime.datetime.now().strftime("The date is: %A %B %Y")

    elif message.find("hi") != -1:
        return "Hi"

    elif message.find("whatisthetime") != -1:
        return datetime.datetime.now().strftime("The time is: %I:%M %p")

    elif message.find("bye") != -1:
        return "See you later"







>>>>>>> Stashed changes
