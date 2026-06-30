import random

def game():
    # choices = ["Foot", "Nuke", "Cockroach"]
    totalRound = 0
    youWin = 0
    tie = 0
    while True:
        
        # userChoice
        userChoice = input("Foot, Nuke or Cockroach? (Quit ends): ")
        if userChoice == "Quit":
            print(f"You played {totalRound} rounds, and won {youWin} rounds, playing tie in {tie} rounds.")
            break
        # Incorrect selection
        if (userChoice != "Nuke" and userChoice != "Foot" and userChoice != "Cockroach"):
            print("Incorrect selection.")
            continue

        
        print(f"You chose: {userChoice}")
        totalRound+=1
        
        # computerChoice
        computerChoice = random.randint(1,3)
        if computerChoice == 1:
            computerChoice = "Foot"
            print(f"Computer chose: {computerChoice}")
            
        elif computerChoice == 2:
            computerChoice = "Nuke"
            print(f"Computer chose: {computerChoice}")

        elif computerChoice == 3:
            computerChoice = "Cockroach"
            print(f"Computer chose: {computerChoice}")
        

        # Logic if-else
        if userChoice == computerChoice:
            if (userChoice == "Nuke" and computerChoice =="Nuke"):
                print("Both LOSE!")
            else:
                print("It is a tie!")
                tie +=1
        
        # user Win
        elif (userChoice == "Foot" and computerChoice == "Cockroach"):
            print("You WIN!")
            youWin +=1
        elif (userChoice == "Nuke" and computerChoice == "Foot"):
            print("You WIN!")
            youWin +=1
        elif (userChoice == "Cockroach" and computerChoice == "Nuke"):
            print("You WIN!")
            youWin +=1

        #cách 2
        # elif (
        #     (userChoice == "Foot" and computerChoice == "Cockroach") or
        #     (userChoice == "Nuke" and computerChoice == "Foot") or
        #     (userChoice == "Cockroach" and computerChoice == "Nuke")
        # ):
        #     print("You WIN!")
        #     youWin += 1
        

        # computer win
        elif (computerChoice == "Foot" and userChoice == "Cockroach"):
            print("You LOSE!")
        elif (computerChoice == "Nuke" and userChoice == "Foot"):
            print("You LOSE!")
        elif (computerChoice == "Cockroach" and userChoice == "Nuke"):
            print("You LOSE!")
        #Cach 2
        # else:
        #     print("You LOSE!")


if __name__ =="__main__":
    game()