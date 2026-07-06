import math

print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))

while True: 
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
    print(f"Current numbers: {num1} {num2}")
    choice = int(input("Please select something (1-8): "))
    if choice == 1: print("The result is: ", num1+num2)
    elif choice == 2: print("The result is: ", num1-num2)
    elif choice == 3: print("The result is: ", num1*num2)
    elif choice == 4: print("The result is: ", num1/num2)
    elif choice == 5: print("The result is: ", math.sin(num1/num2))
    elif choice == 6: print("The result is: ", math.cos(num1/num2))
    elif choice == 7:
        num1 = int(input("Give the first number: "))
        num2 = int(input("Give the second number: "))
        # print(f"Current numbers: {num1} {num2}")
    elif choice == 8: 
        print("Thank you!")
        break
