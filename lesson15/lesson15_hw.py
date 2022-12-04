#task 1
#Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.

class Person():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old."


person1 = Person("Anna", "Lekunovych", 25)
print(person1.talk())


#task 2
#Doggy age
#Create a class Dog with class attribute `age_factor` equals to 7.

class Dog():
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * self.age_factor

dog1 = Dog(8)
print(dog1.human_age())





