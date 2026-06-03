# Exercise 25 - Parameters

def add(a, b):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid Input"

    return a + b


result = add(5, 3)

print("Sum:", result)