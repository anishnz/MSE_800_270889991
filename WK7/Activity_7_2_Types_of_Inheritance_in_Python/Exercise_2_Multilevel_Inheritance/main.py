# ============================================================
# Exercise 2 - University Student Information System
# ============================================================
#
# DEFINITION: Multilevel Inheritance
# -----------------------------------
# Multilevel inheritance is a type of inheritance where a class is
# derived from a child class, which itself was derived from another
# parent class - forming a CHAIN of more than one level.
#
#            Person                     <-- grandparent (top level)
#               |
#            Student                    <-- parent / child of Person
#               |
#       PostgraduateStudent             <-- child of Student, grandchild of Person
#
# Each level adds its OWN extra attribute, while still keeping
# everything defined above it in the chain.
# ============================================================


class Person:
    """Top-level (base) class. Every person has a name."""

    def __init__(self, name):
        self.name = name

    def display_details(self):
        print(f"Name           : {self.name}")


class Student(Person):
    # Student inherits from Person -> LEVEL 1 of the chain.

    def __init__(self, name, student_id):
        # super() here refers to Person (the class directly above Student).
        super().__init__(name)
        self.student_id = student_id  # extra attribute added at this level

    def display_details(self):
        super().display_details()          # reuse Person's printing logic
        print(f"Student ID     : {self.student_id}")


class PostgraduateStudent(Student):
    # PostgraduateStudent inherits from Student -> LEVEL 2 of the chain.
    # Because Student already inherits from Person, PostgraduateStudent
    # automatically gets BOTH Person's and Student's attributes/methods.

    def __init__(self, name, student_id, research_topic):
        # super() here refers to Student (the class directly above this one).
        # This call to Student.__init__ will ITSELF call Person.__init__
        # internally, so all three levels get initialised correctly.
        super().__init__(name, student_id)
        self.research_topic = research_topic  # new attribute at this level

    def display_details(self):
        super().display_details()                     # runs Student -> Person chain
        print(f"Research Topic : {self.research_topic}")


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
if __name__ == "__main__":
    pg_student = PostgraduateStudent(
        name="Bimal Shrestha",
        student_id="STU2025",
        research_topic="Machine Learning in Healthcare",
    )

    print("---- Postgraduate Student Details ----")
    pg_student.display_details()

    # Because of multilevel inheritance, pg_student is an instance
    # of ALL three classes in the chain:
    print("\nIs pg_student a Person?              ", isinstance(pg_student, Person))
    print("Is pg_student a Student?             ", isinstance(pg_student, Student))
    print("Is pg_student a PostgraduateStudent? ", isinstance(pg_student, PostgraduateStudent))
