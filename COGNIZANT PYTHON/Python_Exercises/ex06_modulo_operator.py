# Exercise 6

def check_even_odd(number):

    if not isinstance(number, int):
        print("Invalid Number")
        return

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


number = 17

check_even_odd(number)