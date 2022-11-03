# program that generates a random number between 1 and 10 and lets the user guess what number was generated

import random

message = int(input("Let's find out if you can guess the correct number. Type number from 1 to 10: "))
computer = random.randint(1,10)

if message == computer:
    print("You are a lucky one!")
else:
    print("Sorry, it's not your day. Try again.")

