#task 1

def with_index(iterable, start=0):
    while start < len(iterable):
        for element in iterable:
            yield element, start
            start += 1


k = ["a", "b", "c", "d"]
a = with_index(k)
for item in a:
    print(item)

#task 2

class Range1:

    def __init__(self, start, stop, step=1):
        self.stop = stop
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start
        self.start += self.step
        return current

obj1 = Range1(1, 10, 6)

for item in obj1:
    print(item)


#task 3

class MyIterable:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        self.element = self.iterable.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.element):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.element[index]


n = MyIterable("Implementation of an iterable")

for element in n:
    print(element)



