import csv

total = 0
count = 0

print("STUDENT PERFORMANCE ANALYSIS")

with open("student_marks.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        marks = [
            int(student["Python"]),
            int(student["Java"]),
            int(student["Maths"])
        ]

        average = sum(marks) / len(marks)
        total += average
        count += 1

        print(student["Name"], "Average:", round(average, 2))

print("Total Students:", count)
print("Class Average:", round(total / count, 2))

