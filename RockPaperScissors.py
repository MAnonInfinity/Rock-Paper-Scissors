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

choicesASCII=[rock, paper, scissors]
choices=["Rock", "Paper", "Scissors"]

userChoice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

compChoice=random.randint(0, 2)

print(f"You chose : {choices[userChoice]}\n{choicesASCII[userChoice]}\n Computer Chose : {choices[compChoice]}\n{choicesASCII[compChoice]}")

if userChoice==compChoice:
    print("Game Draw!")
elif userChoice==0:
    if compChoice==2:
        print("You Win!")
    else:
        print("You Lost!")
elif userChoice==1:
    if compChoice==2:
        print("You Lost!")
    else:
        print("You Win!")
elif userChoice==2:
    if compChoice==1:
        print("You Win!")
    else:
        print("You Lose!")
