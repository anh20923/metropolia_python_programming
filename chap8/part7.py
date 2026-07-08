def numbergetter():
    while True:
        try:
            numbervalue = input("Give a numeric value: ")
            numbervalue = float(numbervalue)
            return numbervalue

        except Exception:
            print("Erroneous input, try again.")


def main():
    print("Please type in the full salary")
    salary = numbergetter()

    print("Input the amount of taxes (0-100)")
    taxes = numbergetter()

    leftover = salary * ((100 - taxes) / 100)

    print("You are left with", leftover, "euroes.")


if __name__ == "__main__":
    main()