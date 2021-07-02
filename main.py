# Omar Mehmood Calculator 6/27/2021

print('1)Addition\n2)Subtraction\n3)Multiplication\n4)Division')
selection = int(input("\nSELECTION: "))

if selection == 1:
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(num1 + num2)

if selection == 2:
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(num1 - num2)

if selection == 3:
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(num1 * num2)

if selection == 4:
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(num1 / num2)
