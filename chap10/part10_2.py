shoppingLists = []
while True:
    print("Would you like to")
    choice = int(input("(1)Add or\n(2)Remove items or\n(3)Quit?: "))
    if choice ==1:
        addItem = input("What will be added?: ")
        shoppingLists.append(addItem)

    elif choice == 2:
        print(f"There are {len(shoppingLists)} items in the list.")
        deleteItem = int(input("Which item is deleted?: "))
        #if (deleteItem > len(shoppingLists) -1): 
        if deleteItem < 0 or deleteItem >= len(shoppingLists):
            print("Incorrect selection.")
        else:
            shoppingLists.pop(deleteItem)
        
    elif choice == 3:
        print("The following items remain in the list:")
        for item in shoppingLists:
            print(item)
        break

    else:
        print("Incorrect selection.")

