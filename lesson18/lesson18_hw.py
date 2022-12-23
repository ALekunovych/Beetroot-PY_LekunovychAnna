#task 1

import re

class Validator:

    def __init__(self, email):
        self.validate(email)

    def validate(self, email):
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(pat, email):
            print("Valid Email")
        else:
            print("Invalid Email")

c = Validator(".abc@mail.com")
c1 = Validator("abc.def@mail-archive.com")

#task 2   ??????

# class Boss:
#
#     def __init__(self, id_: int, name: str, company: str):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.workers = []
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.]
#
#
#
# class Worker:
#
#     name = Boss()
#
#     def __init__(self, id_: int, name: str, company: str, boss: Boss):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.boss = boss
#
#     @property
#     def w_name(self):
#         return self.name


#task 3

from functools import wraps

class TypeDecorators:


    def __call__(self, *args, **kwargs):
        return self

    def to_int(func):
        @wraps(func)
        def wrapper(*args):
            return int(func(*args))

        return wrapper

    def to_str(func):
        @wraps(func)
        def wrapper(*args):
            return str(func(*args))

        return wrapper

    def to_bool(func):
        @wraps(func)
        def wrapper(*args):
            return bool(func(*args))

        return wrapper

    def to_float(func):
        @wraps(func)
        def wrapper(*args):
            return float(func(*args))

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string

print(do_nothing('25'))
print(do_something('True'))