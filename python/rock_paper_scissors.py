#Rock, Paper and Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if chose < 0 or chose >= 3:
    print("Invalid Number. You Lost!")
else:
    print(game_images[chose])

    computer_chose = random.randint(0,2)
    print("Computer Chose:")
    print(game_images[computer_chose])


    if chose == 0 and computer_chose == 2:
        print("You win!")
    elif chose == 2 and computer_chose == 0:
        print("You lost!")
    elif chose < computer_chose:
        print("You lost!")
    elif chose > computer_chose:
        print("You win!")
    elif chose == computer_chose:
        print("It was a draw!")