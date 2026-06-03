class Category:

    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount

        if self.spent > self.limit:
            print("Budget Exceeded!")

food = Category("Food", 5000)

food.add_expense(3000)
food.add_expense(2500)

print("Spent:", food.spent)