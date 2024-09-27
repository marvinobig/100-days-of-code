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
choices = [rock, paper, scissors]
userChoice = int(input("What's your play? (0 = rock, 1 = paper, 2 = scissors)"))
computersChoice = random.randint(0, len(choices) - 1)

if userChoice == computersChoice:
    print(f"""
You chose: \n{choices[userChoice]}
The computer chose: \n{choices[computersChoice]}\n
Result: Draw
""")
elif userChoice == 0 and computersChoice == 2:
    print(f"""
You chose: \n{choices[userChoice]}
The computer chose: \n{choices[computersChoice]}\n
Result: You Win!!
""")
elif userChoice == 2 and computersChoice == 1:
    print(f"""
You chose: \n{choices[userChoice]}
The computer chose: \n{choices[computersChoice]}\n
Result: You Win!!
""")
elif userChoice == 1 and computersChoice == 0:
    print(f"""
You chose: \n{choices[userChoice]}
The computer chose: \n{choices[computersChoice]}\n
Result: You Win!!
""")
else:
    print(f"""
You chose: \n{choices[userChoice]}
The computer chose: \n{choices[computersChoice]}\n
Result: You Lose. Game Over!!
""")