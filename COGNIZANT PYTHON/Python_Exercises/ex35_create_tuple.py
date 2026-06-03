# Exercise 35 - Create Tuple

def display_coordinates(coords):

    if len(coords) != 2:
        print("Invalid Coordinates")
        return

    print(f"X = {coords[0]}, Y = {coords[1]}")


coordinates = (10, 20)

display_coordinates(coordinates)