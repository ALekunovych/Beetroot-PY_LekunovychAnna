# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random

list1 = []
list2 = []
i = 0
while i < 10:
    list1.append(random.randint(0, 10))
    list2.append(random.randint(0, 10))
    i += 1
print("List 1 is: ", list1, "\nList 2 is: ", list2)
print("List of the common numbers: ", list(set(list1) & set(list2)))


# if we use list comprehension
# common_numbers2 = [number for number in set(list1) & set(list2) ]
# print(common_numbers2)

