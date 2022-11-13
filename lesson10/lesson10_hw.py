#task1
def oops():
    raise IndexError

def our_func():
    try:
        oops()
    except IndexError:
        print("You have exceeded the line length")

our_func()


#task 2

def action():
    while True:
        try:
            a = int(input("Please type 1st number: "))
            b = int(input("Please type 2nd number: "))
            return a ** 2 / b
        except ValueError:
            print("Please use only integers")
        except ZeroDivisionError:
            print("2nd number shouldn't be 0, try again")


print(action())
