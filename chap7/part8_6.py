import time
while True:
    print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n")
    choice = int(input("Please select one: "))
    if choice == 1: 
        with open("notebook.txt" , "r") as file:
            print(file.read())
            print()
    elif choice == 2:
        writeNote = input("Write a new note: ")
        timeNote = time.strftime("%X %x")
        with open("notebook.txt" , "w") as file:
            file.write(writeNote + ":::" + timeNote)
    elif choice == 3:
        with open("notebook.txt" , "a") as file:
            file.seek(0) # sets  point at the beginning of the file
            file.truncate() # Clear previous content
    elif choice == 4:
        print("Notebook shutting down, thank you.")
        break