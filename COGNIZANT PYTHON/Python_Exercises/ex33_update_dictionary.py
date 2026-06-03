# Exercise 33 - Update Dictionary

def merge_employee_data(emp1, emp2):

    emp1.update(emp2)

    print("Updated Employee Data:")
    print(emp1)


employee1 = {"name": "Ashwin", "age": 21}
employee2 = {"salary": 50000}

merge_employee_data(employee1, employee2)