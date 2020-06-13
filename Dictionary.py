from PyDictionary import PyDictionary

def dict_look_up(lookup):

    dictionary = PyDictionary()
    definition = dictionary.meaning(lookup)
    print (lookup + ": " + str(definition))

