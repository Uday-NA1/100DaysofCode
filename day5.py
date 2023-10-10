import random
# For loop in Python Lists
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(f"{fruit} pie")

# For loops and the range() function
for number in range(1, 11, 3):
    print(number)
    
total = 0
for number in range(1, 101):
    total += number
print(total)

# Final Project: Python Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator")
i_letters = int(input(f"How many letters would you like in your password?\n"))
i_symbols = int(input(f"How many symbols would you like?\n"))
i_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, i_letters + 1):
    password_list.append(random.choice(letters))
    
for char in range(1, i_symbols + 1):
    password_list.append(random.choice(symbols))
    
for char in range(1, i_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for i in password_list:
    password += i
    
print(f"Your password is: {password}")