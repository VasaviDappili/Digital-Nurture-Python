# Exercise 32 - Append to List

def add_expense(expenses, amount):

    if amount <= 0:
        print("Invalid Expense")
        return

    expenses.append(amount)

    print("Updated Expenses:", expenses)


expenses = [100, 200, 300]

add_expense(expenses, 400)