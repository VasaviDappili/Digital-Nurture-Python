# Exercise 30 - Try Except

def divide(a, b):

    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero")


divide(10, 2)
divide(10, 0)