def tester(givenstring):
    if len(givenstring) >= 10 and "X" in givenstring:
        return True
    else:
        return False


def main():
    while True:
        value = input("Write something (quit ends): ")
        if (value == "quit"):
            break
        elif (len(value) < 10):
            print("Too short")
        else:
            print(value)
            if(tester(value) == True):
                print("X spotted!")
        

if __name__ == "__main__":
    main()