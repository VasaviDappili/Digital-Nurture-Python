# Exercise 15 - Nested If

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