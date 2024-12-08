#This is a simple rock-paper-scissors game where the computer randomly chooses from a list


import random

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

choices = [0, 1, 2]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")

if user_choice == 0:
    print(rock)

    if computer_choice == 0:
        print(rock)
        print("It's a draw.")

    elif computer_choice == 1:
        print(paper)
        print("You lose.")

    else:
        print(scissors)
        print("You win.")


elif user_choice == 1:
    print(paper)

    if computer_choice == 0:
        print(rock)
        print("You win.")

    elif computer_choice == 1:
        print(paper)
        print("It's a draw.")

    else:
        print(scissors)
        print("You lose.")


elif user_choice == 2:
    print(scissors)

    if computer_choice == 0:
        print(rock)
        print("You lose.")

    elif computer_choice == 1:
        print(paper)
        print("You win.")
        
    else:
        print(scissors)
        print("It's a draw.")