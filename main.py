import random
import time
import os

while True:
    num = random.randint(0, 1000)
    os.system('cls')
    guess = int(input("Enter a number from 0 - 1000. Press enter to see if it was correct"))
    if guess == num:
        print("Correct! You Guessed the Right Number!")
        input('press enter to exit')
        time.sleep(1.5)
    else:
        print("Incorrect! You Guessed Wrong! :(")
        print("The Correct Number Is: ")
        print(num)
        time.sleep(1.5)
