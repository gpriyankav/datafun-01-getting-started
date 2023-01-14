"""
Optional bonus. See course site for details.

"""

import random

# Change the name below to a name of your choice

name = "GameBot"

# Fix the code below to print the name using an f-string

print()
print("Hello, I'm {Priyanka}, your gamebot.")
print("Let's play an animal guessing game!")
print("There are 3 animals: wolf, eagle, snake (a Python of course).")
print("The wolf scares the eagle.")
print("The eagle grabs the snake.")
print("The snake bites the wolf.")
print("I'll pick one and you pick one and we'll see who wins.")
print()

# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function

"""user_choice = "wolf" """
user_choice = input("Enter any 3 animals-Choose from wolf,eagle and snake:")

# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()


# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!
if user_choice == buddy_choice:
    print("Choosen same try another!")
elif user_choice == "wolf" and buddy_choice == "eagle":
    print("Super!you won")
elif user_choice == "eagle" and buddy_choice == "snake":
    print("Super!you won")
elif user_choice == "wolf" and buddy_choice == "snake":
    print("Super!you won")
else:
    print("Sorry you lost!play again")

# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into the
# docstring comment below.
# --------------------------------------------------------------------
"""

This is Priyanka Gorentla - Date : 1/14/2023. 
I have written the code by checking 2 choices, one user and another random one

Winning selection- 
eagle vs snake - eagle
wolf vs eagle - wolf
snake vs wolf - wolf

"""
