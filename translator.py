from googletrans import Translator
translator = Translator()

def translate(language, message):
    try: 
        thisdict = {'arabic':'ar', 'bengali' : 'bn', 'chinese' : 'zh-CN', 'croatian' : 'hr', 'czech' : 'cs', 'danish' : 'da', 'dutch' : 'nl', 'english' : 'en', 'french' : 'fr','german' : 'de', 'greek':'el', 'hindi':'hi', 'icelandic':'is', 'indonesian':'id', 'irish':'ga', 'italian':'it', 'japanese':'ja', 'korean':'ko', 'kurdish':'ku', 'latin':'la', 'latvian':'lv', 'lithuanian':'lt', 'mongolian':'mn', 'persian':'fa', 'polish':'pl', 'portuguese':'pt', 'punjabi':'pa', 'romanian':'ro', 'russian':'ru', 'spanish':'es', 'turkish':'tr', 'ukrainian':'uk', 'vietnamese':'vi', 'zulu':'zu' }
        language=thisdict[language]
        outmessage = translator.translate(message, dest=language)
        return outmessage.text
    except KeyError:
        return "Language might be mispelled!"
