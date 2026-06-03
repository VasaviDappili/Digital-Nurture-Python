# Exercise 18 - Break Statement

def first_even(start, end):

    if start > end:
        print("Invalid Range")
        return

    for i in range(start, end + 1):
        if i % 2 == 0:
            print("First Even Number:", i)
            break


first_even(1, 10)