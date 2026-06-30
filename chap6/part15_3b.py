def tester(givenstring = "Too short"):
    print (givenstring)


def main():
    while True:
        value = input("Write something (quit ends): ")
        if (value == "quit"):
            break
        elif (len(value) < 10):
            tester()
        elif(len(value) >=10):
            tester(value)
        

if __name__ == "__main__":
    main()