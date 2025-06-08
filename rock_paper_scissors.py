# import random module
# --------------------------------------------
import random

# define the range in which to test 3 numbers
# --------------------------------------------
# random.randint(1, 3)


# Assign Rock (1), Paper (2), Scissors (3) variables
# --------------------------------------------

Rock = 1
Paper = 2
Scissors = 3
# Draw = 4

# Variables assigned tp Ascii Characters
# --------------------------------------------

play_rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


play_paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


play_scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

# Create variable to assign the random numbers
# --------------------------------------------
random_rpc_choice = random.randint(1, 3)
print(random_rpc_choice)

# Create if, elif, else conditionals to decide who wins by the rules of Rock, Paper, Scissors
# --------------------------------------------

if random_rpc_choice == 1:
    print("Rock")
    if Rock == 1 and Paper == 2:
        print("Paper Beats Rock")
        print(play_paper)
        print(play_rock)
    # # Draw Rock
    # # --------------------------------------------
    #
    # elif Rock == 1 and Draw == 4:
    #     print("Draw")
    #     print(play_rock)
    #     print(play_rock)
    else:
        print("Rock beats Scissors")
        print(play_rock)
        print(play_scissors)

elif random_rpc_choice == 2:
    print("Paper")
    if Paper == 2 and Scissors == 3:
        print("Scissors beats Paper")
        print(play_scissors)
        print(play_paper)

    # # Draw Paper
    # # --------------------------------------------
    # elif Paper == 2 and Draw == 4:
    #     print("Draw")
    #     print(play_paper)
    #     print(play_paper)

    else:
        print("Rock beats Scissors")
        print(play_rock)
        print(play_scissors)


elif random_rpc_choice == 3:
    print("Scissors")
    if Rock == 1 and Scissors == 3:
        print("Rock beats Scissors")
        print(play_rock)
        print(play_scissors)

    # # Draw Scissors
    # # --------------------------------------------
    # elif Scissors == 4 and Draw == 4:
    #     print("Draw")
    #     print(play_scissors)
    #     print(play_scissors)

    else:
        print("Paper beats Rock")

# Draw Code (Put this oce into the options above)
# --------------------------------------------

# elif Rock == 1 and Rock == 1:
#     print("Draw")
#     print(play_rock)
#     print(play_rock)
#
# elif Paper == 2 and Paper == 2:
#     print("Draw")
#     print(play_paper)
#     print(play_paper)
#
# elif Scissors == 3 and Scissors == 3:
#     print("Draw")
#     print(play_scissors)
#     print(play_scissors)

else:
    print("Draw: Game Over")
    exit()

