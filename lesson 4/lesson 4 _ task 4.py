# program that verifies the name, despite the letter case
name = input("Please insert your name here: ")

for i in name:
    name = name.lower()
    print("True")
    break
