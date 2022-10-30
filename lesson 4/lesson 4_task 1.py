# Sample String: 'helloworld' / Expected Result : 'held'

a1 = 'helloworld'
i = 0

while i < len(a1):
    print(a1[0] + a1[1] + a1[-2] + a1[-1])
    i += 1
    break

#Sample String: 'my' / Expected Result : 'mymy'

a2 = "my"
i = 0
while i < len(a2):
    print(a2[0] + a2[1], end="")
    i += 1



# Sample String: 'x' /Expected Result: Empty String

b1 = "x"
i = 0
if len(b1) < 2:
    print("\nEmpty string")