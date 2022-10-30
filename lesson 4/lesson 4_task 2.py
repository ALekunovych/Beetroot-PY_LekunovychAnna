#check that the string contains only numerical characters and is only 10 characters long
number = "3805011223"
if number.isdigit() and len(number) == 10:
    print("number is correct")
elif number.isdigit() or len(number) != 10:
    print("number doesn't meet requirements")
else:
    print("number doesn't meet requirements")

