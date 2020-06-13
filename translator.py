from googletrans import Translator

def translate(language, message):
    outmessage = Translator.translate(message, dest='en')
    print (outmessage.text)
