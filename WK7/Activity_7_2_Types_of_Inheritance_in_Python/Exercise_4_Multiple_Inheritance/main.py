# ============================================================
# Exercise 4 - University Student Academic + Contact Information
# ============================================================
#
# DEFINITION: Multiple Inheritance
# -----------------------------------
# Multiple inheritance is a type of inheritance where ONE child class
# inherits from MORE THAN ONE parent class at the same time.
#
#     AcademicInfo       ContactInfo      <-- two separate parents
#              \             /
#               \           /
#                 Student                 <-- one child, inherits BOTH
#
# The Student class below does not fit neatly under a single parent -
# it needs BOTH academic details and contact details, so it inherits
# from both AcademicInfo and ContactInfo at once.
# ============================================================


class AcademicInfo:
    """First parent class: holds a student's academic information."""

    def __init__(self, programme, gpa):
        self.programme = programme
        self.gpa = gpa

    def display_academic_info(self):
        print(f"Programme : {self.programme}")
        print(f"GPA       : {self.gpa}")


class ContactInfo:
    """Second parent class: holds a student's contact information."""

    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

    def display_contact_info(self):
        print(f"Email     : {self.email}")
        print(f"Phone     : {self.phone}")


class Student(AcademicInfo, ContactInfo):
    # Listing BOTH AcademicInfo and ContactInfo inside the parentheses
    # (separated by a comma) is what creates MULTIPLE INHERITANCE.
    # Student now has access to everything from BOTH parent classes.

    def __init__(self, name, programme, gpa, email, phone):
        # NOTE: With multiple inheritance, super() follows Python's
        # Method Resolution Order (MRO), which can be tricky when both
        # parents define __init__. To keep it simple and explicit, we
        # call EACH parent class's __init__ directly by name instead.
        AcademicInfo.__init__(self, programme, gpa)
        ContactInfo.__init__(self, email, phone)

        # name is a new attribute that belongs only to Student.
        self.name = name

    def display_details(self):
        print(f"Name      : {self.name}")
        # These two methods are inherited from the two different parents:
        self.display_academic_info()   # comes from AcademicInfo
        self.display_contact_info()    # comes from ContactInfo


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
if __name__ == "__main__":
    student1 = Student(
        name="Priya Sharma",
        programme="BSc Computer Science",
        gpa=3.8,
        email="priya.sharma@example.edu",
        phone="98-1234-5678",
    )

    print("---- Student Details (Academic + Contact) ----")
    student1.display_details()

    # Student is an instance of BOTH parent classes at once:
    print("\nIs student1 an AcademicInfo?", isinstance(student1, AcademicInfo))  # True
    print("Is student1 a ContactInfo?  ", isinstance(student1, ContactInfo))    # True

    # The Method Resolution Order (MRO) shows the lookup chain Python
    # uses to find attributes/methods across multiple parent classes:
    print("\nMethod Resolution Order (MRO):")
    for cls in Student.__mro__:
        print(" ->", cls.__name__)
