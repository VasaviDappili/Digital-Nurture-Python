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