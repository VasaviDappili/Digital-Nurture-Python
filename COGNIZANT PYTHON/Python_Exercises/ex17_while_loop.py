# Exercise 17 - While Loop

def countdown(count):

    if count <= 0:
        print("Invalid Count")
        return

    while count > 0:
        print(count)
        count -= 1


countdown(5)