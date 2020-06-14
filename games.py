import message_handler
import random
import asyncio
import restart_app
from random import randint

game_enabled = False

async def init_games(client, message):
    global game_enabled
    game_enabled = True
    await message.channel.send("GAME MENU")
    await message.channel.send("1. Play word jumble")
    await message.channel.send("2. Play the monster game")
    await message.channel.send("3. Exit/Quit ")
    await message.channel.send("What would you like to do? ")
    @client.event
    async def on_message(message2):
        if message2.content.lower() == "1":
            await game_1(client, message)
        elif message2.content.lower() == "2":
            await game_2(client, message)
        elif message2.content.lower() == "3":
            await message.channel.send("Ok Quitting....")
            game_enabled = False
            restart_app.restart_program()

async def game_1(client, message):
    global game_enabled
    WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone" ,"different", "language", "mammal", "dessert", "stomach",  "probably", "neither", "numeral", "million", "message", "except", "laughter", "inventor", "journey", "bake", "must", "fried", "rip", "sea", "chase", "bee", "seven", "counting", "write", "steer", "tenth", "they", "fight", "birthday")
    word = random.choice(WORDS)
    print(word)
    correct = word
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    await message.channel.send("Welcome to WORD JUMBLE!!! Unscramble the leters to make a word.")
    await message.channel.send("The jumble is: " + jumble)
    await message.channel.send("Your guess: ")
    guess = ""

    
    @client.event
    async def on_message(message2):
        global game_enabled
        guess = message2.content.lower()
        if game_enabled:
            if message2.author == client.user:
                return
            elif guess == correct:
                await message.channel.send("That's it, you guessed it!\n")
                await message.channel.send("Thanks for playing")
                game_enabled = False
                restart_app.restart_program()
                return
            elif guess == "":
                print("waiting")
            elif guess != correct:    
                await message.channel.send("Voops, thats not rrrrrrright")
                guess = "" 
        else:
            print('exiting')
            
            return

    return

score = 0
async def game_2(client, message):
    global score
    global game_enabled
    game_enabled = True
    await message.channel.send("Monster Game")
    await message.channel.send("There are three doors ahead... ")
    await message.channel.send("There is a monster behind one ")
    await message.channel.send("Which do you choose to open?")

    

    await message.channel.send("Door 1, 2 or 3:  ")

    global score

    @client.event
    async def on_message(message2):
        global score
        guess = message2.content.lower()
        if message2.author == client.user:
            return
        monster_door = randint (1,3)
        door_num = int(guess)
        if door_num <= 3 and door_num >0 and door_num == monster_door:
            await message.channel.send("Monster")
            await message.channel.send("Run away!")
            await message.channel.send("Game over, you scored: " + str(score))
            restart_app.restart_program()
        elif door_num <=3 and door_num >0: 
            await message.channel.send("No monster")
            await message.channel.send("You enter the next room.")
            score+=1
            await message.channel.send("Please enter a number between 1-3")





