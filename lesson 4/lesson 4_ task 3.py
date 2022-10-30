# mathematical expression quiz
welcome_message = """ Hello! Let's take few minutes to solve a short quiz:
15 * 2 = x \n"""
print(welcome_message)
message2 = "What is the correct answer to expression?"
print(message2)
answer_range = ["A. 35", "B. 30", "C. 42", "D. 45"]
print(answer_range[0])
print(answer_range[1])
print(answer_range[2])
print(answer_range[3])

message3 = "\nWrite your answer here:\n"
print(message3)

x = "B. 30"
print(x)

if x == answer_range[0]:
    print("Sorry, answer is incorrect. Try again")
elif x == answer_range[1]:
    print("Your answer is Correct!")
elif x == answer_range[2]:
    print("Sorry, answer is incorrect. Try again")
elif x == answer_range[3]:
    print("Sorry, answer is incorrect. Try again")

