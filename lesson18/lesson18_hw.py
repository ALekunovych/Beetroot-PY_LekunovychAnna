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

#task 2
class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers_list(self):
        return self._workers

    @workers_list.setter
    def workers_list(self, worker):
        if isinstance(worker, Worker):
            if self.company == worker.company:
                self._workers.append(worker)
        else:
            print("This is not worker")


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __str__(self):
        return f"ID: {self.id}; Name: {self.name}; Company: {self.company}; Boss name: {boss.name} "

b1 = Boss(76, "Aiman", "SLB")
b2 = Boss(648, "Ruslan", "SLB")
w1 = Worker(234, "Anna", "SLB", b1)
b1.workers_list = w1
b1.workers_list = b2
print(b1.workers_list)

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