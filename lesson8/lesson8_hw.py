#task1
#A simple function which takes a string containing the name of your favorite movie.
def favourite_movie(x):
    print("My favourite movie is: ", x)

favourite_movie(input("Type your favourite movie here: "))

#task2
# Function that takes country's name and capital as parameters and creates a dict out of it. Function should print the values of the dict
def make_country(name, capital):
    my_dict = {}
    my_dict["name"] = name
    my_dict["capital"] = capital
    print("The capital of", name, "is", capital, end=".")

make_country("Ukraine", "Kyiv")

#task3
#A simple calculator.which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter.  Then return the sum or product of all the numbers in the arbitrary parameter.

def make_operation(operator, number1, number2):
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    else:
        result = number1 * number2
    return result

operator = input("Type operation to be performed (+|-|*): ")
number1 = int(input("The 1st number: "))
number2 = int(input("The 2nd number: "))
print(make_operation(operator, number1, number2))
