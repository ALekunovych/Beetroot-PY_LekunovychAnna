# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string

import random


s = input("Type your word here: ")
b = list()
i = 0
while i < len(s):
    shuffled_string = ''.join(random.sample(s, len(s)))
    b.append(shuffled_string)
    i += 1
print(b)



