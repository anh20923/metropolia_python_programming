import random

print("5 coin flips:")
for i in range (0,5):
    randomChoice = random.randint(0,1)
    if randomChoice == 1:
        print("Heads!")
    else:
        print("Tails!")