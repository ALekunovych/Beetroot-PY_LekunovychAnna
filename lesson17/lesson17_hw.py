# Task 1
# Method overloading.

class Animal:

    def talk(self):
        pass


class Dog(Animal):

    def talk(self):
        print("Woof woof")


class Cat(Animal):

    def talk(self):
        print("Meow")


def func(n):
    return n.talk()


# task2


class Author:

    def __init__(self, name, country, birthday):
        self.books = []
        self.birthday = birthday
        self.country = country
        self.name = name

    def written_new_book(self, book):
        if book not in self.books:
            self.books.append(book)

    def __repr__(self):
        return f"Object of the Author class: {self.name}"

    def __str__(self):
        return f"Name: {self.name}; Country: {self.country}; Date of birth: {self.birthday}; Books: {self.books}"


class Book:
    all_books = []

    def __init__(self, name, year, author: object):
        self.author = author
        self.year = year
        self.name = name
        Book.all_books.append(self.name)

    def all(self):
        return f'Number of all books: {len(Book.all_books)}'

    def __repr__(self):
        return f"Object of the Book class: {self.name}"

    def __str__(self):
        return f"Book: {self.name}; Author: {self.author}, Year: {self.year}"


class Library:

    def __init__(self, name):
        self.name = name
        self.authors = []
        self.books_list = []

    def new_book(self, name: str, year: int, author: object):
        new_b = Book(name, year, author)
        author.written_new_book(new_b)
        if new_b not in self.books_list:
            self.books_list.append(new_b)
            if author not in self.authors:
                self.authors.append(author)
            return new_b
        else:
            print("This book already exist in library. You can find it on the shelves.")

    def group_by_author(self, author: Author):
        return [book for book in self.books_list if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books_list if book.year == year]

    def __repr__(self):
        return f"Object of a Library class: {self.name}"

    def __str__(self):
        return f"This is the '{self.name}' library"



# task 3

import math


class Fraction:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x * other.y + self.y * other.x
        y = self.y * other.y
        common = math.gcd(x, y)
        return Fraction(int(x) // common, int(y) // common)

    def __sub__(self, other):
        x = self.x * other.y - self.y * other.x
        y = self.y * other.y
        common = math.gcd(x, y)
        return Fraction(int(x) // common, int(y) // common)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        common = math.gcd(x, y)
        return Fraction(int(x) // common, int(y) // common)

    def __truediv__(self, other):
        x = self.x * other.y
        y = self.y * other.x
        common = math.gcd(x, y)
        return Fraction(int(x) // common, int(y) // common)

    def __eq__(self, other):
        a = self.x * other.y
        b = other.x * self.y
        return a == b

    def __le__(self, other):
        a = self.x * other.y
        b = other.x * self.y
        return a <= b

    def __lt__(self, other):
        a = self.x * other.y
        b = other.x * self.y
        return a < b

    def __str__(self):
        return f'{self.x} / {self.y}'


if __name__ == "__main__":
    # task1
    c = Cat()
    d = Dog()
    func(c)
    # task2
    l1 = Library("Carturesti")
    print(l1)
    a1 = Author("Stephen King", "USA", 1965)
    a2 = Author("Richard Osman", "UK", 1970)
    print(l1.new_book("Night Shift", 1997, a1))
    print(l1.new_book("It", 1995, a1))
    print(l1.new_book("Thursday Murder Club", 2019, a2))
    print(l1.new_book("It", 2000, a1))
    print(l1.group_by_author(a1))
    print(l1.group_by_year(1995))
    # task3
    x = Fraction(3, 5)
    y = Fraction(2, 4)
    print(x + y)
    print(x - y)
    print(x * y)
    print(y / x)
    print(x == y)
    print(x >= y)
    print(x < y)
