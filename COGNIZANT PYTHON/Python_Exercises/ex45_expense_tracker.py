import csv
from collections import defaultdict

expenses = defaultdict(float)

with open("expenses.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        category = row["category"]
        amount = float(row["amount"])

        expenses[category] += amount

print("Expense Summary")

for category, total in expenses.items():
    print(category, ":", total)