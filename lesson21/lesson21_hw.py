import unittest
# task 1


class FileContextManager:
    counter = 0

    def __init__(self, file_name, mod):
        self.file_name = file_name
        self.mod = mod
        self.file = None

    @classmethod
    def counted_usage(cls):
        return cls.counter

    def __enter__(self):
        try:
            self.file = open(self.file_name, self.mod)
            print("open")
            FileContextManager.counter += 1
        except:
            print("No such file")
        finally:
            return self

    def write(self, sentence):
        self.file.write(sentence)

    def read(self):
        content = self.file.read()
        return content

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"Closing file. Total number of successful operations is {self.counter}")
            print(self.file)
            self.file.close()
        return True


with FileContextManager("lesson21.txt", "w") as context_manager:
    print(context_manager.counted_usage())

with FileContextManager("lesson21.txt", "r") as context_manager:
    print(context_manager.counted_usage())


# task 2


def func_writing(sentence):
    with FileContextManager("lesson21.txt", "w") as context_manager:
        return context_manager.write(sentence)


def func_reading():
    with FileContextManager("lesson21.txt", "r") as context_manager:
        content = context_manager.read()
        return content


func_writing("Hello World")


class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(func_reading(), "Hello World")


if __name__ == '__main__':
    unittest.main()
