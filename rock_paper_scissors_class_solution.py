# import random module
# --------------------------------------------
import random

# define the range in which to test 3 numbers
# --------------------------------------------
# random.randint(0, 2)


# Assign Rock (0), Paper (1), Scissors (2) variables
# --------------------------------------------

Rock = 0
Paper = 1
Scissors = 2

# Variables assigned tp Ascii Characters
# --------------------------------------------

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Assign Ascii images to a variable
# -----------------------------------------

game_images = [rock, paper, scissors]


# Assign 0, 1, 2 for paper (0) rock (1) scissors (1) options
# 0, 1, 2
# -----------------------------------------

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if user_choice >= 0 or user_choice <= 2:
    print(game_images[user_choice])


# Create variable to assign the random numbers
# --------------------------------------------
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Display user's choice
# --------------------------------------------

if user_choice >= 3 or user_choice < 0:
    print("You typed and invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("User wins!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("Computer wins!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("It's a draw!")
