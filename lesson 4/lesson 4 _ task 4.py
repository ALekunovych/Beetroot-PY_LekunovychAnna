# program that verifies the name, despite the letter case

a = ["Anna", "Anton", "Yulia", "Valentyn"]

name = input("Please enter your name: ")

for i in a:
    if i.lower() == name.lower():
        print(f"Hello, {i}!")
        break
else:
    print("User not found")




