import pickle
import time

try:
    with open("notebook.dat", "rb") as file:
        notes = pickle.load(file)
except:
    notes = []
    print("No default notebook was found, created one.")


while True:
    print("(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit\n")
    choice = int(input("Please select one: "))
    if choice == 1:
        for note in notes:
            print(note)

    elif choice == 2:
        writeNote = input("Write a new note: ")
        timeNote = time.strftime("%X %x")
        notes.append(writeNote + ":::" + timeNote)

    elif choice == 3:
        print(f"The list has {len(notes)} notes.")
        changeSelection = int(input("Which of them will be changed?: "))
        if changeSelection < 0 or changeSelection >=len(notes):
            print("Incorrect selection")
        else:
            print(notes[changeSelection])
            newNote = input("Give the new note: ")
            timeNote = time.strftime("%X %x")
            notes[changeSelection] = newNote + ":::" + timeNote

    elif choice == 4:
        print(f"The list has {len(notes)} notes.")
        deleteNote = int(input("Which of them will be deleted?: "))
        if deleteNote < 0 or deleteNote > len(notes):
            print("Incorrect selection")
        else:
            deleted = notes.pop(deleteNote - 1)
            print(f"Deleted note {deleted}") 

    elif choice == 5:
        with open("notebook.dat", "wb") as file:
            pickle.dump(notes, file)

        print("Notebook shutting down, thank you.")
        break






# import pickle
# import time

# notes=[]
# print("No default notebook was found, created one.")
# while True:
#     print("(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Empty the notebook\n(5) Save and quit\n")
#     choice = int(input("Please select one: "))
#     if choice == 1: 
#         try: 
#             with open("notebook.dat" , "rb") as file:
#                 readdata = pickle.load(file)
#                 print(readdata)
#         except FileNotFoundError:
#              pass

#     elif choice == 2:
#         writeNote = input("Write a new note: ")
#         timeNote = time.strftime("%X %x") 
#         with open("notebook.dat" , "wb") as file:
#             data = pickle.dump(writeNote + ":::" + timeNote, file)
        
#         notes.append(data)

#     elif choice == 3:
#         print(f"The list has {len(notes)} notes.")
#         changeSelection = int(input("Which of them will be changed?: "))
#         if changeSelection < 0 or changeSelection >=len(notes):
#             print("Incorrect selection")
#         else:
#             print(notes[changeSelection])
#             newNote = input("Give the new note: ")
#             with open("notebook.dat" , "wb") as file:
#                 data = pickle.dump(newNote + ":::" + timeNote, file)

#     elif choice == 4:
#         print(f"The list has {len(notes)} notes.")
#         deleteNote = int(input("Which of them will be deleted?: "))
#         if deleteNote < 0 or deleteNote > len(notes):
#             print("Incorrect selection")
#         else:
#             print(f"Deleted note {notes[deleteNote]}") 

#     elif choice == 5:
#                 print("Notebook shutting down, thank you.")
#                 break
