import ai

name = input("Enter a username: ")
print ("Hello, " + name)
print ("")
while True:
  choice = input("Would you like to play word jumble? ").upper()
  if choice == "YES" or choice == "Y":
    break
  elif choice == "NO" or choice == "N":
    print("That's a shame! Have a nice day")
    print ("")
  else:
    print("Please Answer only Yes or No")
    continue
print ("")
print (26 * "-", "WORD JUMBLE MENU", 26 * "-")
print ("1. Play game")
print ("2. Exit/Quit ")
print ("What would you like to do? ")
print ("")


answer = True
while answer:
  answer= input("Option 1, 2: ") 

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

  
  elif answer=="2":
    print ("That's a shame. Thanks for playing!\n") 
  elif answer=="":
    print("Not Valid Choice Try again")