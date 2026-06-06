print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))

while True: 
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit")
    print(f"Current numbers: {num1} {num2}")
    choice = int(input("Please select something (1-6): "))
    if choice == 1: print("The result is: ", num1+num2)
    elif choice == 2: print("The result is: ", num1-num2)
    elif choice == 3: print("The result is: ", num1*num2)
    elif choice == 4: print("The result is: ", num1/num2)
    elif choice == 5:
        num1 = int(input("Give the first number: "))
        num2 = int(input("Give the second number: "))
        # print(f"Current numbers: {num1} {num2}")
    elif choice == 6: 
        print("Thank you!")
        break

