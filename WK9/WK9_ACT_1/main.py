# ============================================================
# Exercise: Student Result Management (CORRECTED, after debugging)
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. Ask the user for the name and three subject marks (Maths, Science,
#      English) of five students. Each student becomes one dictionary
#      {"name": ..., "marks": [...], "average": ...} appended to a list.
#   2. A student's average = the sum of THEIR OWN marks divided by the
#      number of subjects. This must be computed fresh for every student,
#      using only that student's marks - nothing carried over from
#      before.
#   3. A student has Passed if average >= 50, otherwise Failed.
#   4. class_average = the sum of every student's average divided by the
#      number of STUDENTS (not the number of subjects).
#   5. The student with the highest average is found with
#      max(students, key=...).
#
# This is the corrected program. buggy_version.py is the first attempt:
# it ran without crashing but printed the wrong averages and the wrong
# class average. QUESTION_AND_ANSWER.txt explains both bugs and how
# Python Tutor (https://pythontutor.com/) was used to find them.
# ============================================================

SUBJECTS = ["Maths", "Science", "English"]
NUM_STUDENTS = 5
PASS_MARK = 50


def read_student(position):
    """Ask for one student's name and marks, return their result record."""
    name = input(f"Enter name of student {position}: ")

    marks = []
    for subject in SUBJECTS:
        mark = float(input(f"  Enter {subject} mark for {name}: "))
        marks.append(mark)

    # Fix for Bug 1: total/average is a NEW local calculation for this
    # student only. Nothing from a previous student can leak into it.
    total = sum(marks)
    average = total / len(marks)

    return {"name": name, "marks": marks, "average": average}


def main():
    students = [read_student(i + 1) for i in range(NUM_STUDENTS)]

    print("\n--- Results ---")
    for student in students:
        status = "Passed" if student["average"] >= PASS_MARK else "Failed"
        print(f"{student['name']}: average = {student['average']:.2f} -> {status}")

    # Fix for Bug 2: divide by the number of STUDENTS, not the number of
    # subjects.
    class_average = sum(student["average"] for student in students) / len(students)
    print(f"\nClass average: {class_average:.2f}")

    topper = max(students, key=lambda s: s["average"])
    print(f"Highest average: {topper['name']} ({topper['average']:.2f})")


if __name__ == "__main__":
    main()
