def tester(givenstring = "Too short"):
    return givenstring


def main():
    while True:
        value = input("Write something (quit ends): ")
        if (value == "quit"):
            break
        elif (len(value) < 10):
            print(tester())
        elif(len(value) >=10):
            print(tester(value))
        

if __name__ == "__main__":
    main()