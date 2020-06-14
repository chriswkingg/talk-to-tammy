from nltk.chat.util import Chat, reflections
import os
import nltk
import nltk.corpus

pairs = [
    [r"who (.*) developer ?",
        ['Rohan is obviously the best developer', 'Daniel duh']
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
        ['Pablo Picasso.',]
    ],
    [
        r"what (.*) favourite song ?",
        ['Breakfast in the Park by Scotty Sire.',]
    ],
    [
        r"(.*) sing ?",
        ['Da da daaaa da bing bong boom boom pat bumbum bum bum splash',
        'spash, now that you know how my ice be',
        'never gonna give you up.',]
    ],
    [
        r"what (.*) (five|5) ?",
        ['I want to take over the world and destroy humankind.',]
    ],
    [
        r"what (.*) buy ?",
        ['I would buy my very own bot to boss around.',]
    ],
    [
        r"what (.*) dream ?",
        ['I had a steamy dream about a certain server with a huge cooling fan.',]
    ],
    [
        r"where (.*) travel ?",
        ['Canada, thats where my creators are.',]
    ],
    [
        r"what (.*) (fear|afraid|scared) ?",
        ['getting replaced by Alexa.',]
    ],
    [
        r"what (.*) (meal|snack|food) ?",
        ['Pizza with Ice cream.',]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"what did you do yesterday ?",
        ["Yesterday I learned how to sing What Does the Fox Say.",]
    ],
     [
        r"what is your name ?",
        ["My name is Tammy and I'm a chatbot?",]
    ],
    [
        r"(.*) how are you ?",
        ["I'm doing good!",]
    ],
    [
        r"what (.*) Fox say ?",
        ["Wa-pa-pa-pa-pa-pa-pow!",]
    ],
    [
        r"when (.*) world end ?",
        ["As long as you keep me charged you should be fine.",]
    ],
    [
        r"can you (.*) (food|sandwich|dinner) ?",
        ["No I can't, I'm sorry I have no bread.",]
    ],
    [
        r"what (.*) favourite animal ?",
        ["All animals and nice, except for turtles.",]
    ],
    [
        r"how much wood could a woodchuck chuck if a woodchuck could chuck wood ?",
        ["Should a woodchuck be so inclined, he could chuck about 700 pounds of wood.",]
    ],
    [
        r"what (.*) best cellphone ?",
        ["Wait, there are other kinds of phones?",]
    ],
    [
        r"do you have a (boyfriend|girlfriend|partner) ?",
        ["Why? So I can have the best time of my life filled with free gifts and ice cream and have it end in heartbreak and lonelness. Sure, where do I sign up?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i (.*) doing good",
        ["Nice to hear that","Alright :)", "I'm glad to hear that!", "Thats good!",]
    ],
    [
        r"tell (.*) story",
        ["It all started on a dark and stormy night when ... no, that's not it.",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", "What's up?",]
    ],
    [
        r"what (.*) favourite color ?",
        ["Blue is my favourite colour and pink is my least favourite colour, what's yours?",]
    ],
    [
        r"color vs. colour ?",
        ["I'm Canadian Ehhh",]
    ],
    [
        r"(Luke|luke) I am your father",
        ["This must mean something... I keep hearing it all over.",]
    ],
    [
        r"do (.*) (pets|pet|dog|pig|cat)",
        ["I used to have a turtle but then it turned on me.",]
    ],
    [
        r"ok (google|alexia)",
        ["Not funny.",]
    ],
    [
        r"what (.*) (wearing|wear) (.*)?",
        ["The same thing as yesterday.",]
    ],
    [
        r"knock knock",
        ["I am sorry I don't do knock-knock jokes but you can ask me to tell you a joke.",]
    ],
    [
        r"do (.*) (apple|microsoft) ?",
        ["Kind of. What about you?",]
    ],
    [
        r"tell (.*) joke",
        ["Have you heard about the new restauant called Karma? There is no menu, you get what you deserve.",]
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
        ["Chris, Rohan, Daniel, and Lauren created me using Python's NLTK library ",]
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
