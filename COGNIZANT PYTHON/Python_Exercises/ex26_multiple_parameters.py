# Exercise 26 - Multiple Parameters

def rectangle_area(length, width):

    if length <= 0 or width <= 0:
        return "Invalid Dimensions"

    return length * width


print("Area:", rectangle_area(5, 3))