#task3

def count_lines():
    with open("colors.txt", "r") as file:
        print("Number of lines in the file is: ", len(file.readlines()))

def count_chars():
    with open("colors.txt", "r") as file:
#       count = [char for char in file.read().replace("\n", "").replace(" ", "")]   #excluding whitespaces and new lines \n
        print(len(file.read()))

def my_test():
    count_lines()
    count_chars()

# count_lines()
# count_chars()
def main():
    my_test()


if __name__ == "__main__":
    main()
