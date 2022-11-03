# Use input to generate: “Hello <name>, on your next birthday you’ll be <age+1> years”

name = input("Please add your name here: ")
age = int(input("And don't forget to mention your age: "))

print(f"Hello {name}, on your next birthday you'll be {age + 1} years old.")