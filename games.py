import ai
import random
import message_handler
import discord
from random import randint 
async def playGame(message):
  author = message.author
  channel = message.channel
  voicechannel = author.voice.channel
  name = author.name
  await message.channel.send("Hello, " + name)
  await message.channel.send("1. Play word jumble")
  await message.channel.send("2. Play the monster game")
  await message.channel.send("3. Exit/Quit ")
  await message.channel.send("What would you like to do? ")

  
  while True:
    answer=message.content.lower().replace('$', '')
    #print(answer)
    
    
    if answer=="1": 
      
        
    elif answer=="2": 
      await message.channel.send("Monster Game")
      await message.channel.send("There are three doors ahead... ")
      await message.channel.send("There is a monster behind one ")
      await message.channel.send("Which do you choose to open?")
      feeling_brave = True 
      score = 0
      while feeling_brave:
        monster_door = randint (1,3)
        door = input("Door 1, 2 or 3:  ")
        door_num = int(door)
        if door_num <= 3 and door_num >0 and door_num == monster_door:
          await message.channel.send("Monster")
          feeling_brave = False 
        elif door_num <=3 and door_num >0: 
          await message.channel.send("No monster")
          await message.channel.send("You enter the next room.")
          score+=1
        else:
          await message.channel.send("Please enter a number between 1-3")
      await message.channel.send("Run away!")
      await message.channel.send("Game over, you scored", score)
      await message.channel.send("")

    elif answer=="3":
      await message.channel.send("That's a shame. Thanks for playing!\n") 
    elif answer=="":
      await message.channel.send("Not Valid Choice Try again")