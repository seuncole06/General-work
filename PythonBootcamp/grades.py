students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68]
]

for student in students:
    name = student[0]
    score1 = student[1]
    score2 = student[2]
    score3 = student[3]

    total = score1 + score2 + score3
    average = total / 3

    if average >= 70:
        grade = "Grade A"
    elif average >= 60:
        grade = "Grade B"
    elif average >= 50:
        grade = "Grade C"
    elif average >= 45:
        grade = "Grade D"
    elif average >= 40:
        grade = "Grade E"
    else:
        grade = "Grade F"

    print(f"{name} - {average:.2f} - {grade}")