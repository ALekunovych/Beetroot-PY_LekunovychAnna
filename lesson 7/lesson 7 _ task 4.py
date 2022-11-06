# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

list1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

new_dict = {i+1: list1[i] for i in range(0, 7) }
print(new_dict)

my_dict = {}

for key in new_dict:
    my_dict[new_dict[key]] = key
print(my_dict)


# via list comprehension
# my_dict2 = {list1[i]: i+1 for i in range(0, 7) }
# print(my_dict2)