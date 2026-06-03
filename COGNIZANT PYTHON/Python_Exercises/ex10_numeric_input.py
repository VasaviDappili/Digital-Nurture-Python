# Exercise 10

def next_year_age():

    age = input("Enter your age: ")

    if not age.isdigit():
        print("Please enter a valid number")
        return

    age = int(age)

    print("Next year you'll be", age + 1)


next_year_age()