from pprint import pprint

# task1
#School
#Make a class structure in python representing people at school

class Person(object):

    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

class Student(Person):

        def __init__(self, name, surname, age, gender, hobby, start_year, performance):
            super().__init__(name, surname, age, gender)
            self.hobby = hobby
            self.start_year = start_year
            self.performance = performance

        def record(self):
            dict = {"Name": self.name,
                    "Surname": self.surname,
                    "Age": self.age,
                    "Gender": self.gender,
                    "Hobby": self.hobby,
                    "Admission year": self.start_year,
                    "Performance level": self.performance}
            return dict


class Teacher(Person):

    def __init__(self, name, surname, age, gender,  subject, seniority, salary):
        super().__init__(name, surname, age, gender)
        self.subject = subject
        self.seniority = seniority
        self.salary = salary

    def record(self):
        dict = {"Name": self.name,
                "Surname": self.surname,
                "Age": self.age,
                "Gender": self.gender,
                "Subject": self.subject,
                "Seniority": self.seniority,
                "Salary": self.salary}
        return dict

stud1 = Student("Vadym", "Babiy", 12, "Male", "basketball", 2005, "A")
stud2 = Student("Alina", "Korobko", 10, "Female", "piano", 2006, "B")
teach1 = Teacher("Tamara", "Voloshko", 49, "Female", "Mathematics", 20, 20000)
teach2 = Teacher("Olga", "Martynova", 50, "Female", "Literature", 28, 20100)
pprint(stud1.record())
pprint(stud2.record())
pprint(teach1.record())
pprint(teach2.record())


# Task 2
# Mathematician

class Base(object):

    def __init__(self, list1, list2, list3):
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3

class Mathematician(Base):

    def square_nums(self):
        return list(map(lambda x: x**2, self.list1))

    def remove_positives(self):
        return list(filter(lambda x: x < 0, list2))

    def filter_leaps(self):
        return list(filter(lambda x: x % 4 == 0, list3))

list1 = [7, 11, 5, 4]
list2 = [26, -11, -8, 13, -90]
list3 = [2001, 1884, 1995, 2003, 2020]
m = Mathematician(list1, list2, list3)
print(m.square_nums())
print(m.remove_positives())
print(m.filter_leaps())


# Task 4
# Custom exception

class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", "a") as file:
            file.write(self.msg)

try:
    case1 = int(input("Type number from 1 to 5: "))
    if not 0 < case1 < 5:
        raise CustomException("My custom exception for case1\n")
except:
    pass

try:
    case2 = input('Type letter "A": ')
    if not case2 == "A":
        raise CustomException("My custom exception for case2\n")
except:
    pass