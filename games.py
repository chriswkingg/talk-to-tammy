import ai

def input_handler(message):
    if message.find("games") != -1:
        return 

name = input("Enter a username: ")
print ("Hello, " + name)
print ("")
print (26 * "-", "GAME MENU", 26 * "-")
print ("1. Play word jumble")
print ("2. Play the monster game")
print ("3. Exit/Quit ")
print ("What would you like to do? ")
print ("")

answer = True
while answer:
  answer= input("Option 1, 2, 3: ") 

  if answer=="1": 
        import random
        WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
        word = random.choice(WORDS)
        correct = word
        jumble = ""
        while word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]
        print ("")
        print("Welcome to WORD JUMBLE!!! Unscramble the leters to make a word.")
        print ("")
        print("The jumble is:", jumble)
        guess = input("Your guess: ")
        while guess != correct and guess != "":
            print ("")
            print("Sorry, that's not it")
            guess = input("Your guess: ")
        if guess == correct:
            print ("")
            print("That's it, you guessed it!\n")
        print("Thanks for playing")
        print ("")
      
  elif answer=="2": 
      from random import randint 
      print ("Monster Game")
      print ("There are three doors ahead... ")
      print ("There is a monster behind one ")
      print ("Which do you choose to open?")
      feeling_brave = True 
      score = 0
      while feeling_brave:
        monster_door = randint (1,3)
        door = input("Door 1, 2 or 3:  ")
        door_num = int(door)
        if door_num <= 3 and door_num >0 and door_num == monster_door:
          print ("Monster")
          feeling_brave = False 
        elif door_num <=3 and door_num >0: 
          print ("No monster")
          print ("You enter the next room.")
          score+=1
        else:
          print ("Please enter a number between 1-3")
      print ("Run away!")
      print ("Game over, you scored", score)
      print ("")

  elif answer=="3":
    print ("That's a shame. Thanks for playing!\n") 
  elif answer=="":
    print("Not Valid Choice Try again")
