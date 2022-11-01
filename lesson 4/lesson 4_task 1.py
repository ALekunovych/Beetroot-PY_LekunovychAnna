# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

a = input("Type your message here: \n")
if len(a) > 4 :
    a = a[0:2] + a[-2:]
    print(a)
elif len(a) == 2:
    a = a*2
    print(a)
elif len(a) < 2:
    print("")