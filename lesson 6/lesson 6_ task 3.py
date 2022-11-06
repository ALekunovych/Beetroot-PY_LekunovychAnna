# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

list1 = list(range(1, 101))
print(list1)
final_list = []

i = 1
while i in list1:
    if i % 7 == 0 and i % 5 != 0:
        final_list.append(i)
    i += 1
print("Divisible by 7, but not a multiple of 5: ", final_list)

