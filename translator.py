from googletrans import Translator
translator = Translator()

def translate(language, message):
    Dict = dict ({'Arabic'	'ar', 'Bengali' : 'bn', 'Chinese' : 'zh', 'Croatian' : 'hr', 'Czech' : 'cs', 'Danish' : 'da', 'Dutch' : 'nl', 'English' : 'en', 'French' : 'fr','German' : 'de', 'Greek':'el', 'Hindi':'hi', 'Icelandic':'is', 'Indonesian':'id', 'Irish':'ga', 'Italian':'it', 'Japanese':'ja', 'Korean':'ko', 'Kurdish':'ku', 'Latin':'la', 'Latvian':'lv', 'Lithuanian':'lt', 'Mongolian':'mn', 'Persian':'fa', 'Polish':'pl', 'Portuguese':'pt', 'Punjabi':'pa', 'Romanian':'ro', 'Russian':'ru', 'Spanish':'es', 'Turkish':'tr', 'Ukrainian':'uk', 'Vietnamese':'vi', 'Zulu':'zu' })
    dict.get(language)
    outmessage = translator.translate(message, dest=language)
    return outmessage.text
