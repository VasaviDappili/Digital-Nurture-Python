# Exercise 13 - If Else

def check_even_odd(num):

    if not isinstance(num, int):
        print("Invalid Input")
        return

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


num = 8

check_even_odd(num)