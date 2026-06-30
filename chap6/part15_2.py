def poweroftwo(number):
    result = 2**number
    return result

def main():
    inputNumber = int(input("Give a number: "))
    finalResult = poweroftwo(inputNumber)
    print(f"The result is {finalResult}")


if __name__ == "__main__":
    main()