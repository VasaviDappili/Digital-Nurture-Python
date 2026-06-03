# Exercise 23 - Math Module

import math

def circle_area(radius):

    if radius <= 0:
        print("Invalid Radius")
        return

    area = math.pi * radius ** 2

    print(f"Area of Circle: {area:.2f}")


circle_area(5)