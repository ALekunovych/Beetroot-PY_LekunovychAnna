from functools import wraps

#task 1
# Write a decorator that prints a function with arguments passed to it.

def logger(func):
    @wraps(func)
    def decorated(*args):
        numToStr = ','.join([str(elem) for elem in args])
        print(func.__name__ + " was called with " + numToStr)
        # return func(*args)            # uncomment if we want the function to be executed
    return decorated


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


square_all(4, 5, 6, 7)
add(9, 2)

# task 2
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function


def stop_words(words: list):
    def smth(func):
        def decorator(name):
            a = func(name)
            for word in words:
                a = a.replace(word, "*")
            return a
        return decorator
    return smth

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("Steve"))


#task 3
# Write a decorator `arg_rules` that validates arguments passed to the function.


def arg_rules(type_: type, max_length: int, contains: list):
    def smth(func):
        def check(name):
            if type(name) != type_ or len(name) > max_length or any(char not in name for char in contains):
                return "Entered name does not match requirements"
            return func(name)
        return check
    return smth


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("S@SH05"))
print(create_slogan("johndoe05@gmail.com"))
