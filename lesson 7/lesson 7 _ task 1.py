#Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.


sentence = "Unique people have unique life experience"
sentence = sentence.lower().split()
print(sentence)
values = []
our_dict = {}

for i in sentence:
    if i not in values:
        values.append(i)
for i in range(0, len(values)):
    our_dict[values[i]] = sentence.count(values[i])
print(our_dict)


