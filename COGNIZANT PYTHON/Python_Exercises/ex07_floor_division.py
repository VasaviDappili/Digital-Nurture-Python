# Exercise 7

def split_bill(total_bill, people):

    if total_bill <= 0:
        print("Invalid Bill Amount")
        return

    if people <= 0:
        print("Invalid Number of People")
        return

    share = total_bill // people

    print("Individual Share:", share)


total_bill = 1250
people = 4

split_bill(total_bill, people)