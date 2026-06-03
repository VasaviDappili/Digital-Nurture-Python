# Exercise 37 - Multiple Instances

class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee Name:", self.name)


emp1 = Employee("Ashwin")
emp2 = Employee("Rahul")

emp1.display()
emp2.display()