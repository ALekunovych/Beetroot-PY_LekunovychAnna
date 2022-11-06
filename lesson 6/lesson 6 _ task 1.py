# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random

our_list = []
i = 0
while i in range(10):
    numbers = random.randint(0, 100)
    our_list.append(numbers)
    i += 1
print(our_list)
print("The largest number from a list  is:", max(our_list))

