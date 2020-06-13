from googletrans import Translator
translator = Translator()
def translate(message):
    outmessage = translator.translate(message, dest='en')
    return outmessage.text
