import random

# Random Module Overview
random_int = random.randint(1, 10)
print(random_int)

random_float = random.random() * 5
print(random_float)


# Lists in Python

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
                    "Connecticut", "Massachusetts", "Maryland", "South Carolina",
                    "New Hampshire", "Virginia", "New York", "North Carolina",
                    "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio",
                    "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
                    "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
                    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
                    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

number_of_states = len(states_of_america)

print(states_of_america[number_of_states - 1])

# Nested Lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

# Final Project: Rock Paper Scissors

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

rps = [rock, paper, scissors]

user = int(input("Please type '0' for rock, '1' for paper and '2' for scissors.\n"))
if user >=3 or user < 0:
    print("That is invalid!")
else:
    print(rps[user])

    computer = random.randint(0, 2)
    print(f"Computer chose: ")
    print(rps[computer])

    if user == 0 and computer == 2:
        print("You Won!")
    elif computer == 0 and user == 2:
        print("You Lost!")
    elif computer > user:
        print("You Lost!")
    elif user > computer:
        print("You Won!")
    elif computer == user:
        print("You Tied!")