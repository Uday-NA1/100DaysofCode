# Strings: Surrounded by double quotes

print("Hello"[0]) #Subscripting: Pick out numbers from a string | Outcome = "H"

print("123" + "345")

# Integers: Whole numbers
print(123 + 345)

#Floats: Decimal numbers
print(123.25 + 356.25)

#Boolean: True or false

True
False



# Converting Datatypes

num_char = len(input("What is your name? "))
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

print(70 + float("100.5")) # Outcome = 170.5
print(str(70) + str(100)) # Outcome = 70100

# Number Manipulation

print(round(8 / 3 , 2)) # Rounds the number upto 2 decimal points (FLOAT)
print(round(8 // 3)) # Cuts decimal numbers (INTEGER)

result = 4 / 2
result += 10
print(result)

# F-Strings

score = 1

print(f"Your score is: {score}")


# Final Project: Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
people = float(input("How many people to split the bill? "))
tip_as_percentage = tip / 100
total_tip_amount =  bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_tip = "{:.12f}".format(bill_per_person)
print(f"Each person should pay: {final_tip}")




# Mathamatical Operations
6 + 3 # Addition
6 - 3 # Subtraction
6 * 3 # Multiplication
6 / 3 # Division
6 ** 3 # Exponents

# BEDMAS RULE [ORDER OF OPERATIONS]:
# 1 - Brackets [()]
# 2 - Exponents [**]
# 3 - Division [/]
# 4 - Multiplication [*]
# 5 - Addition [+]
# 6 - Subtraction [-]

# ORDER OF OPERATIONS IN PYTHON (ORDER OF IMPORTANCE):
# 1 - Brackets [()]
# 2 - Exponents [**]
# 3 - Division [/] & Multiplication [*]
# 4 - Addition [+] & Subtraction [-]

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)