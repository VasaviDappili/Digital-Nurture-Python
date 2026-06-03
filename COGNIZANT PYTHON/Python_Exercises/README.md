# Cognizant-Python-Exercise

## EX-01:Simple Hello World
### code:
```
print("Hello World!")
```
### output:
<img width="1019" height="145" alt="1 1" src="https://github.com/user-attachments/assets/273d202d-0a38-4244-832e-9fcf3f66b2a7" />

## EX-02:Jupyter Notebook
### code:
print("Hello from Jupyter!")
### output:
<img width="738" height="298" alt="image" src="https://github.com/user-attachments/assets/8577ebce-3840-4b83-9d4f-9506d1bd1488" />

## EX-03:VS Code Setup 
### code:
print("Hello, Python in VS Code!")
### output:
<img width="1265" height="102" alt="image" src="https://github.com/user-attachments/assets/30bf6e9b-ab45-435c-840d-2cad7b0461e5" />

## EX-04:Float Precision
### code:
```
def calculate_net_salary(salary, tax_rate):

    if salary <= 0:
        print("Invalid Salary")
        return

    if tax_rate < 0 or tax_rate > 1:
        print("Invalid Tax Rate")
        return

    tax = salary * tax_rate
    net_salary = salary - tax

    print(f"Net Salary: {net_salary:.2f}")


salary = 75000.5
tax_rate = 0.18

calculate_net_salary(salary, tax_rate)
```
### output:
<img width="1009" height="145" alt="1 4" src="https://github.com/user-attachments/assets/88ae76e2-531e-4c78-9dc4-a5de79946e91" />

## EX-05:Multiple Assignment
### code:
```
def display_coordinates(coords):

    if len(coords) != 2:
        print("Invalid Coordinates")
        return

    x, y = coords

    print("X =", x)
    print("Y =", y)


coordinates = (10, 20)

display_coordinates(coordinates)
```

### output:
<img width="1021" height="162" alt="1 5" src="https://github.com/user-attachments/assets/d8992cc5-6bce-49f0-b85e-487a7b33594e" />

## EX-06:Modulo Operator 
### code:
```
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

```
### output:
<img width="1023" height="121" alt="1 6" src="https://github.com/user-attachments/assets/8f613393-5dd9-45bc-8252-20055244a909" />

## EX-07:Floor Division 
### code:
```
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
```
### output:
<img width="1024" height="141" alt="1 7" src="https://github.com/user-attachments/assets/51a3b0e5-9289-4a0c-8cf4-59d5541b3ba3" />

## EX-08:Min/Max Functions 
### code:
```
def find_salary_range(salaries):

    if not salaries:
        print("Salary list is empty")
        return

    print("Highest Salary:", max(salaries))
    print("Lowest Salary:", min(salaries))


salaries = [50000, 75000, 62000, 95000]

find_salary_range(salaries)
```
### output:
<img width="1024" height="173" alt="1 8" src="https://github.com/user-attachments/assets/942ff960-14e6-4e20-bbc6-5da39e79b368" />


## EX-09:Basic Input 
### code:
```
def greet_user():

    name = input("Enter your name: ")

    if name.strip() == "":
        print("Name cannot be empty")
        return

    print("Hello,", name)


greet_user()
```
### output:
<img width="1018" height="160" alt="1 9" src="https://github.com/user-attachments/assets/8ee71517-c68d-40cb-a1f9-9b434eb76f21" />

## EX-10:Numeric Input
### code:
```
def next_year_age():

    age = input("Enter your age: ")

    if not age.isdigit():
        print("Please enter a valid number")
        return

    age = int(age)

    print("Next year you'll be", age + 1)


next_year_age()
```
### output:
<img width="1022" height="139" alt="1 10" src="https://github.com/user-attachments/assets/ce4f3b23-53b1-45b0-a473-ef3745b3a323" />

## EX-11:Float Input
### code:
```
def kg_to_lbs():

    try:
        kg = float(input("Enter weight in kg: "))

        if kg <= 0:
            print("Invalid Weight")
            return

        lbs = kg * 2.20462

        print(f"Weight in pounds: {lbs:.2f}")

    except ValueError:
        print("Please enter a valid decimal number")


kg_to_lbs()
```
### output:
<img width="1036" height="140" alt="1 11" src="https://github.com/user-attachments/assets/bf100216-3376-4e7f-9a7e-1fa44bf7517b" />

## EX-12:Simple If 
### code:
```
# Exercise 12 - Simple If

def check_pass(marks):

    if marks < 0 or marks > 100:
        print("Invalid Marks")
        return

    if marks >= 35:
        print("Pass")


marks = 75

check_pass(marks)
```
### output:
<img width="1034" height="122" alt="1 12" src="https://github.com/user-attachments/assets/64732230-9f2e-429a-ac95-e323f9cc264a" />

## EX-13:If-Else
### code:
```
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
```
### output:
<img width="1028" height="117" alt="1 13" src="https://github.com/user-attachments/assets/e977cffd-37ff-4a2f-815e-bbd703a59f8f" />

## EX-14:If-Elif-Else
### code:
```
def calculate_grade(score):

    if score < 0 or score > 100:
        print("Invalid Score")
        return

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    else:
        grade = "C"

    print("Grade:", grade)


score = 88

calculate_grade(score)
```
### output:
<img width="1024" height="128" alt="1 14" src="https://github.com/user-attachments/assets/f4e6304e-be86-4eae-b9de-53a387a6f0f4" />

## EX-15:Nested If
### code:
```
def login(user, pwd):

    if user.strip() == "" or pwd.strip() == "":
        print("Username or Password cannot be empty")
        return

    if user == "admin":
        if pwd == "pass123":
            print("Login Successful")
        else:
            print("Wrong Password")
    else:
        print("Invalid Username")


user = "admin"
pwd = "pass123"

login(user, pwd)
```
### output:
<img width="1011" height="118" alt="1 15" src="https://github.com/user-attachments/assets/4746200b-10a9-42fd-ad14-ed709bdfda51" />

## EX-16:For Loop Basics 
### code:
```
def print_numbers(count):

    if count <= 0:
        print("Invalid Count")
        return

    for i in range(count):
        print(i + 1)


print_numbers(5)
```
### output:
<img width="1018" height="214" alt="1 16" src="https://github.com/user-attachments/assets/9310e092-2318-4756-bf37-493d919a6fa9" />

## EX-17:While Loop
### code:
```
def countdown(count):

    if count <= 0:
        print("Invalid Count")
        return

    while count > 0:
        print(count)
        count -= 1


countdown(5)
```
### output:
<img width="1025" height="202" alt="1 17" src="https://github.com/user-attachments/assets/cd395736-59ea-41eb-bce7-c1d6405ab976" />

## EX-18:Break Statement  
### code:
```
def first_even(start, end):

    if start > end:
        print("Invalid Range")
        return

    for i in range(start, end + 1):
        if i % 2 == 0:
            print("First Even Number:", i)
            break


first_even(1, 10)
```
### output:
<img width="1029" height="114" alt="1 18" src="https://github.com/user-attachments/assets/b8d1169a-c099-40d6-b5e0-73552b171fb0" />

## EX-19:Continue Statement
### code:
```
def sum_odd_numbers():

    total = 0

    for i in range(10):

        if i % 2 == 0:
            continue

        total += i

    print("Sum of Odd Numbers:", total)


sum_odd_numbers()
```
### output:
<img width="1022" height="117" alt="1 19" src="https://github.com/user-attachments/assets/fde68398-afa9-4515-b9fc-7cd093741d4e" />

## EX-20:Pass Statement  
### code:
```
def future_feature():
    pass


future_feature()

print("Function defined")
```
### output:
<img width="1025" height="123" alt="1 120" src="https://github.com/user-attachments/assets/3fee5bed-8241-4c00-a678-0d483e8d48f6" />

## EX-21:Consistent Indentation 
### code:
```
def check_nested():
    condition1 = True
    condition2 = True

    if condition1:
        if condition2:
            print("Nested")

    print("Indentation is correct")


check_nested()
```
### output:
<img width="1028" height="140" alt="1 21" src="https://github.com/user-attachments/assets/d25b7f4b-f479-4894-aa74-5f63bda8ac04" />

## EX-22:Comment Usage 
### code:
```
def calculate_salary():

    # Base salary of employee
    base_salary = 50000

    # Bonus amount
    bonus = 10000

    # Total salary calculation
    total_salary = base_salary + bonus

    print("Total Salary:", total_salary)


calculate_salary()
```
### output:
<img width="1027" height="122" alt="1 22" src="https://github.com/user-attachments/assets/c364c12f-f4f2-4db1-9cb7-2c3ebc56fd68" />

## EX-23:Import Standard Module 
### code:
```
import math

def circle_area(radius):

    if radius <= 0:
        print("Invalid Radius")
        return

    area = math.pi * radius ** 2

    print(f"Area of Circle: {area:.2f}")


circle_area(5)
```
### output:
<img width="1024" height="123" alt="1 23" src="https://github.com/user-attachments/assets/fcfca83b-1591-4219-b96f-7d8bb19fb31f" />

## EX-24:All Import 
### code:
```
from math import *

def math_operations(num):

    if num < 0:
        print("Invalid Input")
        return

    print("Square Root:", sqrt(num))
    print("Power:", pow(num, 2))
    print("PI Value:", pi)


math_operations(16)
```
### output:
<img width="1025" height="163" alt="1 24" src="https://github.com/user-attachments/assets/9ed0cdb4-6421-4cee-bb7b-7f5ebdd7d1d5" />

## EX-25:Parameters
### code:
```
def add(a, b):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid Input"

    return a + b


result = add(5, 3)

print("Sum:", result)
```
### output:
<img width="1029" height="116" alt="1 25" src="https://github.com/user-attachments/assets/f67742a3-cec9-4e99-a020-7dd2be648ac5" />

## EX-26:Multiple Parameters  
### code:
```
def rectangle_area(length, width):

    if length <= 0 or width <= 0:
        return "Invalid Dimensions"

    return length * width


print("Area:", rectangle_area(5, 3))
```
### output:
<img width="1022" height="109" alt="1 26" src="https://github.com/user-attachments/assets/ce9870d9-b8d6-4340-b893-a93c42bbfebb" />

## EX-27:Len Function  
### code:
```
def string_length(text):

    if text.strip() == "":
        print("Empty String")
        return

    print("Length:", len(text))


string_length("Python")
```
### output:
<img width="1023" height="121" alt="1 27" src="https://github.com/user-attachments/assets/938276b5-585e-49dd-9bc9-39320606e3cc" />

## EX-28:Write to File
### code:
```
def write_file():

    with open("greeting.txt", "w") as file:
        file.write("Hello World")

    print("Data written successfully")


write_file()
```
### output:
<img width="1020" height="120" alt="1 28" src="https://github.com/user-attachments/assets/16c7d4e0-0aca-4e73-aa99-4a2969cc2f4e" />

## EX-29:Read from File
### code:
```
def read_file():

    try:
        with open("greeting.txt", "r") as file:
            content = file.read()

        print("File Content:")
        print(content)

    except FileNotFoundError:
        print("File not found")


read_file()
```
### output:
<img width="1038" height="146" alt="1 29" src="https://github.com/user-attachments/assets/7a9f5ba6-4f41-400c-8a49-281ea18b647f" />

## EX-30:Basic Try-Except 
### code:
```
def divide(a, b):

    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero")


divide(10, 2)
divide(10, 0)
```
### output:
<img width="1025" height="139" alt="1 30" src="https://github.com/user-attachments/assets/23dbae09-508f-44bc-9597-fb9ccad642d7" />

## EX-31:Create List
### code:
```
def display_cart(cart):

    if not cart:
        print("Cart is empty")
        return

    print("Cart Items:", cart)


cart = [100, 250, 75]

display_cart(cart)
```
### output:
<img width="1020" height="116" alt="1 31" src="https://github.com/user-attachments/assets/dfd41a9e-27de-4b2e-903b-da1cc94e149a" />

## EX-32:Append to List 
### code:
```
def add_expense(expenses, amount):

    if amount <= 0:
        print("Invalid Expense")
        return

    expenses.append(amount)

    print("Updated Expenses:", expenses)


expenses = [100, 200, 300]

add_expense(expenses, 400)
```
### output:
<img width="1025" height="121" alt="1 32" src="https://github.com/user-attachments/assets/6a2b91e1-f149-4d7d-b8bc-7db96a390046" />

## EX-33:Update Dictionary 
### code:
```
def merge_employee_data(emp1, emp2):

    emp1.update(emp2)

    print("Updated Employee Data:")
    print(emp1)


employee1 = {"name": "Ashwin", "age": 21}
employee2 = {"salary": 50000}

merge_employee_data(employee1, employee2)
```
### output:
<img width="1021" height="141" alt="1 33" src="https://github.com/user-attachments/assets/edb8c882-8709-47aa-8c40-ed4b6bbcc869" />

## EX-34:Nested Dictionary
### code:
```
def get_salary(data, department, employee):

    if department not in data:
        print("Department not found")
        return

    if employee not in data[department]:
        print("Employee not found")
        return

    print("Salary:", data[department][employee])


employees = {
    "IT": {
        "Ashwin": 50000,
        "Rahul": 60000
    },
    "HR": {
        "Priya": 45000
    }
}

get_salary(employees, "IT", "Ashwin")
```
### output:
<img width="1020" height="121" alt="1 34" src="https://github.com/user-attachments/assets/e1c3d883-30b6-4431-bf68-303edb1e5e89" />

## EX-35:Create Tuple 
### code:
```
def display_coordinates(coords):

    if len(coords) != 2:
        print("Invalid Coordinates")
        return

    print(f"X = {coords[0]}, Y = {coords[1]}")


coordinates = (10, 20)

display_coordinates(coordinates)
```
### output:
<img width="1018" height="117" alt="1 35" src="https://github.com/user-attachments/assets/aa8cd336-1435-49a1-9df3-a1314dccf64f" />

## EX-36:Set Intersection
### code:
```
def common_skills(set1, set2):

    common = set1 & set2

    print("Common Skills:", common)


skills1 = {"Python", "Java", "SQL"}
skills2 = {"Python", "C++", "SQL"}

common_skills(skills1, skills2)
```
### output:
<img width="1021" height="118" alt="1 36" src="https://github.com/user-attachments/assets/20a920e4-a74f-4997-b44f-6e37290363cc" />

## EX-37:Multiple Instances 
### code:
```
class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee Name:", self.name)


emp1 = Employee("Ashwin")
emp2 = Employee("Rahul")

emp1.display()
emp2.display()
```
### output:
<img width="1019" height="138" alt="1 37" src="https://github.com/user-attachments/assets/af63af45-8ed0-42ba-8d7c-d0d7e1ad68a3" />



## EX-38:Method Chaining
### code:
```
class Employee:

    def __init__(self):
        self.salary = 0

    def set_salary(self, salary):
        self.salary = salary
        return self

    def apply_raise(self, amount):
        self.salary += amount
        return self

    def display(self):
        print("Final Salary:", self.salary)
        return self


emp = Employee()

emp.set_salary(50000).apply_raise(5000).display()
```
### output:
<img width="1022" height="116" alt="1 38" src="https://github.com/user-attachments/assets/44c06e54-d3a0-4748-a6dd-d5b7f662a3aa" />

## EX-39:Polymorphism 
### code:
```
class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer writes code")


class Manager(Employee):
    def work(self):
        print("Manager manages team")


employees = [Developer(), Manager()]

for emp in employees:
    emp.work()
```
### output:
<img width="1021" height="140" alt="1 39" src="https://github.com/user-attachments/assets/0e399ac7-51e6-4b0b-a1a9-f56b97f80798" />

## EX-40:Class Methods 
### code:
```
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):

        name, salary = data.split(",")

        return cls(name, int(salary))

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


emp = Employee.from_string("Shubh,75000")

emp.display()
```
### output:
<img width="1016" height="145" alt="1 40" src="https://github.com/user-attachments/assets/218cf3cd-4cdc-45ea-85c3-c574503e8497" />

## EX-41:Employee Management System 
### code:
```
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
```
### output:
<img width="1018" height="135" alt="1 41" src="https://github.com/user-attachments/assets/0a55e011-b35e-4162-9b9c-0c46569a8eaf" />

## EX-42:Data Analysis Pipeline 
### code:
```
import statistics

try:
    with open("sales.txt", "r") as file:
        sales = [int(line.strip()) for line in file]

    print("Mean:", statistics.mean(sales))
    print("Median:", statistics.median(sales))

except FileNotFoundError:
    print("sales.txt not found")

except ValueError:
    print("Invalid data in file")
```
### output:
<img width="1029" height="155" alt="1 42" src="https://github.com/user-attachments/assets/15a39e1f-9ad2-4179-91c8-59b9584d1588" />

## EX-43:Configuration Manager 
### code:
```
import configparser

class Config:
    pass


class DatabaseConfig(Config):

    def load_config(self):

        config = configparser.ConfigParser()
        config.read("db.ini")

        required = ["host", "user", "password", "database"]

        for key in required:
            if key not in config["DATABASE"]:
                print("Missing key:", key)
                return

        print("Database Configuration Loaded")
        print(dict(config["DATABASE"]))


db = DatabaseConfig()
db.load_config()
```
### output:
<img width="1008" height="109" alt="1 43" src="https://github.com/user-attachments/assets/25a3d32a-b9e7-47fc-a5ca-f86a6a2ef50c" />

## EX-44:CSV Data Processor 
### code:
```
import csv

employees = []

with open("employees.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        row["salary"] = int(row["salary"])
        employees.append(row)

high_salary = [emp for emp in employees if emp["salary"] > 50000]

avg_salary = sum(emp["salary"] for emp in employees) / len(employees)

print("Employees Salary > 50000")
print(high_salary)

print("Average Salary:", avg_salary)
```
### output:
<img width="1022" height="150" alt="1 44" src="https://github.com/user-attachments/assets/3048965c-9bf7-4e58-bdad-e4346f971786" />

## EX-45:Expense Tracker
### code:
```
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
```
### output:
<img width="1003" height="144" alt="1 45" src="https://github.com/user-attachments/assets/8631bd23-6777-4bd6-9e91-542c7d449075" />

## EX-46:API Response Handler 
### code:
```
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true"

try:

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        print("Temperature:",
              data["current_weather"]["temperature"])

        print("Wind Speed:",
              data["current_weather"]["windspeed"])

    elif response.status_code == 404:
        print("Data not found")

    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException:
    print("Network Error")
```
### output:
<img width="1020" height="101" alt="1 46" src="https://github.com/user-attachments/assets/8742c423-1022-4a17-be13-f89c9c4f6661" />

## EX-47:Complete Calculator Program
### code:
```
def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid Operator"
    except ZeroDivisionError:
        return "Cannot divide by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

print("Result:", calculate(a, b, op))
```
### output:
<img width="1029" height="141" alt="1 47" src="https://github.com/user-attachments/assets/8eb88c33-3071-49b1-a033-514dfd202ac1" />

## EX-48:Shopping Cart System
### code:
```
class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.items)
        gst = total * 0.18
        return total + gst

cart = ShoppingCart()

cart.add_item(CartItem("Laptop", 50000, 1))
cart.add_item(CartItem("Mouse", 500, 2))

print("Final Amount:", cart.calculate_total())
```
### output:
<img width="1031" height="71" alt="1 48" src="https://github.com/user-attachments/assets/ffcd80f2-2a6c-4dc2-9106-7e8b7eb4244d" />

## EX-49:Temperature Converter GUI 
### code:
```
class Converter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

temp = float(input("Enter Celsius: "))

obj = Converter()

print("Fahrenheit:", round(obj.c_to_f(temp), 2))
```
### output:
<img width="1018" height="93" alt="1 49" src="https://github.com/user-attachments/assets/c18365ea-4b22-480a-bf2b-90212cc5637a" />

## EX-50:Backup Utility 
### code:
```
import shutil

try:
    shutil.copy("sample.txt", "backup_sample.txt")
    print("Backup Created")

except FileNotFoundError:
    print("Source File Not Found")
```
### output:
<img width="1013" height="75" alt="1 50" src="https://github.com/user-attachments/assets/4ca89346-617e-4757-a24b-df93a58bc755" />

## EX-51:URL Shortener 
### code:
```
import hashlib

class URLShortener:

    def __init__(self):
        self.urls = {}

    def shorten(self, url):
        short = hashlib.md5(url.encode()).hexdigest()[:6]
        self.urls[short] = url
        return short

    def lookup(self, short):
        return self.urls.get(short)

obj = URLShortener()

short = obj.shorten("https://google.com")

print("Short URL:", short)
print("Original URL:", obj.lookup(short))
```
### output:
<img width="1017" height="95" alt="1 51" src="https://github.com/user-attachments/assets/4ffd2f67-7463-41ed-8230-90fb1390ebc6" />

## EX-52:Gradebook System 
### code:
```
students = {
    "Ashwin": [80, 90, 85],
    "Rahul": [70, 75, 80]
}

for student, grades in students.items():

    gpa = sum(grades) / len(grades)

    print(student, "GPA:", round(gpa, 2))

class_avg = sum(sum(g) for g in students.values()) / sum(len(g) for g in students.values())

print("Class Average:", round(class_avg, 2))
```
### output:
<img width="1028" height="122" alt="1 52" src="https://github.com/user-attachments/assets/1f706ee3-8377-45cc-b87b-db132bf68a34" />

## EX-53:Task Scheduler 
### code:
```
from datetime import datetime

tasks = [
    ("Project", "2026-06-10"),
    ("Assignment", "2026-06-05"),
    ("Exam", "2026-06-20")
]

tasks.sort(key=lambda x: datetime.strptime(x[1], "%Y-%m-%d"))

print("Sorted Tasks")

for task in tasks:
    print(task)
```
### output:

<img width="1021" height="151" alt="1 53" src="https://github.com/user-attachments/assets/997c136b-ae04-4c7c-95d5-f89724227f8f" />

## EX-54:Inventory Manager
### code:
```
inventory = {
    "Laptop": 10,
    "Mouse": 3,
    "Keyboard": 2
}

low_stock = {item for item, qty in inventory.items() if qty < 5}

print("Inventory:", inventory)
print("Low Stock Alerts:", low_stock)
```
### output:
<img width="1028" height="106" alt="1 54" src="https://github.com/user-attachments/assets/7349eea1-93a9-4229-843e-a9d6bbb5aac4" />

## EX-55:Budget Planner 
### code:
```
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
```
### output:
<img width="1015" height="114" alt="1 55" src="https://github.com/user-attachments/assets/d05a73db-08db-4e68-be74-242d0574dabf" />

