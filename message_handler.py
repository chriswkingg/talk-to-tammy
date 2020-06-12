
import datetime


def input_handler(message):
    if message.find("$whatisthedate") != -1:
        return datetime.datetime.now().strftime("%B " "%Y")

    elif message.find("$hi") != -1:
        return "Hi"







