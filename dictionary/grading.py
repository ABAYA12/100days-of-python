students_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

stydents_grades = {}

for student in students_score:
    score = students_score[student]
    if score > 90:
        stydents_grades[student] = "Outstanding"
    elif score > 80:
        stydents_grades[student] = "Exceeds Expectations"
    elif score > 70:
        stydents_grades[student] = "Acceptable"
    else:
        stydents_grades[student] = "Fail"

print(stydents_grades)
