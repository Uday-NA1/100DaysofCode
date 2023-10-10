# Here is a small project I made for fun.
def math():
    a = int(input("Type your first number:\n"))
    b = int(input("Type your second number:\n"))
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b
    
    print(f"Both your numbers added: {add}")
    print(f"Both your numbers subtracted: {subtract}")
    print(f"Both your numbers multiplied: {multiply}")
    print(f"Both your numbers divided: {divide}")
    
calculator = input("Do you want to run the calculator? (Y/N)\n")
if calculator == "Y" or calculator == "y":
    math()
elif calculator == "N" or calculator == "n":
    print("OK")
else:
    print('Please type either "Y" or "N"')