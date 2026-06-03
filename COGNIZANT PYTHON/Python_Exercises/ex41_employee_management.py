# Exercise 41 - Employee Management System

import json

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"


employees = {
    "101": {"name": "Ashwin", "salary": 50000},
    "102": {"name": "Rahul", "salary": 60000}
}

with open("emps.json", "w") as file:
    json.dump(employees, file, indent=4)

with open("emps.json", "r") as file:
    data = json.load(file)

for emp_id, details in data.items():
    emp = Employee(emp_id, details["name"], details["salary"])
    print(emp)