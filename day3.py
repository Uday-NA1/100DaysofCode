# If/Else statements and Nested If/Else statements

print("Welcome to the roller coaster")
height = int(input("What is your height in centimetres? "))
age = int(input("What is your age? "))
bill = 0

if height >= 135:
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Teenager tickets are $7.")
    elif age >= 45 and age >= 55:
        print("Everything is going to be ok. Have a free ride with us!")
    else:
        bill = 12
        print("Adult tickets are $12")

    photo = input("Do you want a photo taken? Y or N. ")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")


else:
    print("Sorry, But you are too short and cannot ride the roller coaster.")


# FINAL PROJECT: TREASURE ISLAND

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input("You are on an island. type 'left' to move left or 'right' to move right. ").lower
if left_or_right == "left":
    print("You fell into a pit and died.")
    print("Game over!")
swim_or_wait = input("There is another island nearby. type 'swim' if you want to swim there or 'wait' if you want to wait for a boat. ").lower
if swim_or_wait == "swim":
    print("You where eaten by a shark and died.")
    print("Game over!")
enter_or_wait = input("There is a house. Type 'wait' if you want to wait outside or 'enter' to enter the house. ").lower
if enter_or_wait == "wait":
    print("You waited outside for too long and starved to death.")
    print("Game Over!")
door = input("There are 3 doors. type 'red' if you want to enter the first, 'blue' if you want to enter the second and 'yellow' if you want to enter the third. ").lower
if door == "blue":
    print("You entered a room filled with water and drowned to death.")
    print("Game Over!")
elif door == "red":
    print("You entered a room filled with lava and burned to death")
    print("Game Over!")
print("You have found the treasure in the yellow room!")
print("You Win!")