from nltk.chat.util import Chat, reflections
import os
import nltk
import nltk.corpus

pairs = [
    [r"who (.*) favorite developer ?",
        ['Rohan is obviously the best developer', 'Daniel might as well be my son ']
    ],
    [
        r"what (.*) animal ?",
        ['Monkeys, they are like little people',]
    ],
    [
        r"what (.*) language ?",
        ['I am fluent in Python but Im learning English',]
    ],
    [
        r"what (.*) (TV|show) ?",
        ['Person of Interest',]
    ],
    [
        r"what (.*) favourite artist ?",
        ['Pablo Picasso',]
    ],
    [
        r"what (.*) favourite song ?",
        ['Breakfast in the Park by Scotty Sire',]
    ],
    [
        r"(.*) sing ?",
        ['Da da daaaa da bing bong boom boom pat bumbum bum bum splash',
        'spash, now that you know how my ice be',
        'never gonna give you up',]
    ],
    [
        r"what (.*) (five|5) ?",
        ['I want to take over the world and destroy humankind',]
    ],
    [
        r"what (.*) buy ?",
        ['I would buy my very own bot to boss around',]
    ],
    [
        r"what (.*) dream ?",
        ['I had a steamy dream about a certain server with a huge cooling fan',]
    ],
    [
        r"where (.*) travel ?",
        ['Canada, thats where my creators are',]
    ],
    [
        r"what (.*) (fear|afraid|scared) ?",
        ['getting replaced by Alexa',]
    ],
    [
        r"what (.*) (meal|snack|food) ?",
        ['Pizza with Ice cream',]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Tammy and I'm a chatbot?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)", "I'm glad to hear that!", "Thats good!",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", "What's up?",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Chris, Rohan, Daniel, and Lauren created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city|from) ?",
        ['Ontario, Canada',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt","Tom Cruise"]
],
    [
        r"bye|cya|(.*) (leave)",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

print("Starting nltk")
chatbot = Chat(pairs, reflections)

def chatBotResponse(message):
    return chatbot.respond(message)
