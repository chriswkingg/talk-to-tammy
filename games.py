import message_handler
import random
import asyncio

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
            await message2.channel.send("Chris has big pp")

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