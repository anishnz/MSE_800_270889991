# ============================================================
# Student Result Management - FIRST ATTEMPT (contains 2 bugs)
# ============================================================
#
# This is the version that was pasted into Python Tutor
# (https://pythontutor.com/) and stepped through with the Forward
# button. It does NOT crash - it runs to the end and prints numbers -
# but the numbers are wrong. That is what makes this kind of bug
# dangerous: nothing raises an exception, so the mistake has to be
# caught by watching the variables change, not by reading an error.
#
# See QUESTION_AND_ANSWER.txt for:
#   - exactly which two lines are wrong and why
#   - how stepping through in Python Tutor pointed at each one
#   - the corrected version (also in main.py)
# ============================================================

SUBJECTS = ["Maths", "Science", "English"]
NUM_STUDENTS = 5
PASS_MARK = 50

students = []

# "total" is created ONCE here, before the student loop even starts.
total = 0

for i in range(NUM_STUDENTS):
    name = input(f"Enter name of student {i + 1}: ")
    marks = []

    for subject in SUBJECTS:
        mark = float(input(f"  Enter {subject} mark for {name}: "))
        marks.append(mark)
        total += mark  # BUG 1: this keeps adding onto every earlier student's marks too

    average = total / len(SUBJECTS)  # uses the ever-growing "total", not just this student's marks
    students.append({"name": name, "marks": marks, "average": average})

print("\n--- Results ---")
for student in students:
    status = "Passed" if student["average"] >= PASS_MARK else "Failed"
    print(f"{student['name']}: average = {student['average']:.2f} -> {status}")

class_total = sum(student["average"] for student in students)
class_average = class_total / len(SUBJECTS)  # BUG 2: should divide by the number of STUDENTS
print(f"\nClass average: {class_average:.2f}")

topper = max(students, key=lambda s: s["average"])
print(f"Highest average: {topper['name']} ({topper['average']:.2f})")
