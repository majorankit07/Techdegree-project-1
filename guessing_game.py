"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

print("""
    ---------------------
    Welcome to the number Guessing Game!")
    ---------------------
    """)

highscore = 10

    


name = input("What is your name?  ")
print("Hello {}! Welcome to the number guessing game!".format(name))

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    random_number = random.randint(1,10)
    guess = 0
    no_of_attempts = 0


    global highscore

    while guess != random_number:
      try:
        guess = int(input("Pick a number between 1 and 10: "))
        no_of_attempts += 1
        if guess > 10:
          print("Invalid input! Please enter a number between 1 - 10")
        elif guess < 1:
          print("Invalid input! Please enter a number between 1 - 10")
        elif guess > random_number:
            print("It is lower!")
        elif guess < random_number:
            print("It is higher!")
            continue
         

        else:
          print("You got it! It took you {} tries.".format(no_of_attempts))  
          
          new_game = input("Would you like to play again? [y]es/[n]o: ")
          if no_of_attempts < highscore:
            highscore = no_of_attempts
          if new_game.lower() == 'y':
            print("The HIGHSCORE is {}".format(highscore))
            start_game()
      except ValueError:
        print("Oh no! Please enter a number between 1-10") 
    else:
      print()


# Kick off the program by calling the start_game function.
start_game()
print("Thank you! You are a winner!")