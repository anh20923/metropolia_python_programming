def getnumber():
    mynumber = input("Give a numeric value: ")
    return mynumber


def main():
    number1 = getnumber()
    number2 = getnumber()

    try:
        result = int(number1) / int(number2)

    except ZeroDivisionError:
        print("Its not possible to divide with 0.")

    except (TypeError, ValueError):
        print("Its not possible to calculate letters.")

    else:
        print("The result is", result)


if __name__ == "__main__":
    main()