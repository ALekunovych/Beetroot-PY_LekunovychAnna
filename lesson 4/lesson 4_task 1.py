# Sample String: 'helloworld' / Expected Result : 'held'

a = input("Type your message here: \n")
if len(a) > 4 :
    a = a[0:2] + a[-2:]
    print(a)
elif len(a) == 2:
    a = a*2
    print(a)
elif len(a) < 2:
    print("")