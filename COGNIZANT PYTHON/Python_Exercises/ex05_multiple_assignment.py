

def display_coordinates(coords):

    if len(coords) != 2:
        print("Invalid Coordinates")
        return

    x, y = coords

    print("X =", x)
    print("Y =", y)


coordinates = (10, 20)

display_coordinates(coordinates)