import random

num = random.randint(0,1000)

guess = input("Enter a number from 0 - 1000. Press enter to see if it was correct")
if guess == num:
    print("Correct! You Guessed the Right Number!")
    input("Press enter to exit")
else:
    print("Incorrect! You Guessed Wrong! :(")
    print("The Correct Number Is: ")
    print(num)
    input("Press enter to exit")
