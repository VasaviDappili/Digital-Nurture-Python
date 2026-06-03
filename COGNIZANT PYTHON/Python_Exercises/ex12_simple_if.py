# Exercise 12 - Simple If

def check_pass(marks):

    if marks < 0 or marks > 100:
        print("Invalid Marks")
        return

    if marks >= 35:
        print("Pass")


marks = 75

check_pass(marks)