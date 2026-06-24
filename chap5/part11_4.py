while True:
    print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n")
    choice = int(input("Please select one: "))
    if choice == 1:
        with open("notebook.txt", "r") as file:
            print(file.read())
        
    elif choice == 2:
        writeText = input("Write a new note: ")
        with open("notebook.txt", "a") as file:
            file.write(writeText + "\n")
    elif choice == 3:
        with open("notebook.txt", "w") as file:
            file.write("")
            print("Notes deleted.")
    elif choice == 4:
        print("Notebook shutting down, thank you.")
        break