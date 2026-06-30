# -*- coding: cp1252 -*-

from random import randint
import sys

def numbergame():
    number = randint(0, 100)

    while True:

        guess = int(input("Give a number between 0-100: "))

        if guess < 0:
            print("Bad guess!")
            print("Program is terminated.")
            sys.exit(0)

        if guess == number:
            print("You guessed correctly!")
            break
        elif guess < number:
            print("The number is larger than that.")
        else:
            print("The number is smaller than that.")

if __name__ == "__main__":
    numbergame()