# import mymodule
# def main():
#     salary = int(input("Give monthly salary: "))
#     tax = int(input("Give tax percentage (0-100): "))

#     result = mymodule.taxcalculator(salary, tax)

#     print("You'll get", result, "euros.")

# if __name__ == "__main__":
#     main()



from mymodule import taxcalculator
def main():
    salary = int(input("Give monthly salary: "))
    tax = int(input("Give tax percentage (0-100): "))

    result = taxcalculator(salary, tax)

    print("You'll get", result, "euros.")

if __name__ == "__main__":
    main()