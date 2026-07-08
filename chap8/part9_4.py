import time
def checkNoteBook():
    fileName = "notebook.txt"

    try:
        with open(fileName, "r") as file:
            pass

    except FileNotFoundError:
        print("No default notebook was found, created one.")
        with open(fileName, "w") as file:
            pass

    return fileName

def changeNoteBook():
    fileName = input("Give the name of the new file: ")

    try:
        with open(fileName, "r") as file:
            pass

    except FileNotFoundError:
        print("No notebook with that name detected, created one.")
        with open(fileName, "w") as file:
            pass

    return fileName


def main():
    fileName = checkNoteBook()
    while True:
        print("Now using file", fileName)
        print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit\n")
        choice = int(input("Please select one: "))

        if choice == 1: 
            with open(fileName , "r") as file:
                print(file.read())
                print()

        elif choice == 2:
            writeNote = input("Write a new note: ")
            timeNote = time.strftime("%X %x")
            with open(fileName , "a") as file:
                file.write(writeNote + ":::" + timeNote)

        elif choice == 3:
            with open(fileName , "a") as file:
                file.seek(0) # sets  point at the beginning of the file
                file.truncate() # Clear previous content

        elif choice ==4:
            fileName = changeNoteBook()

        elif choice == 5:
            print("Notebook shutting down, thank you.")
            break


if __name__ == "__main__":
    main()
    