# Exercise 14 - Grade Calculator

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