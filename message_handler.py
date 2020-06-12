
import datetime


def input_handler(message):
    if message.find("$whatisthedate") != -1:
        return datetime.datetime.now().strftime("The date is: %A %B %Y")

    elif message.find("$hi") != -1:
        return "Hi"

    elif message.find("$whatisthetime") != -1:
        return datetime.datetime.now().strftime("The time is: %I:%M %p")







