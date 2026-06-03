students = {
    "Ashwin": [80, 90, 85],
    "Rahul": [70, 75, 80]
}

for student, grades in students.items():

    gpa = sum(grades) / len(grades)

    print(student, "GPA:", round(gpa, 2))

class_avg = sum(sum(g) for g in students.values()) / sum(len(g) for g in students.values())

print("Class Average:", round(class_avg, 2))