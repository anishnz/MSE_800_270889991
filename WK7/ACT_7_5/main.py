# ============================================================
# Example: University and Department Using Composition
# ============================================================
#
# DEFINITION: Composition
# -----------------------------------
# Composition models a "has-a" relationship: a University HAS-A
# Department, rather than a University BEING a Department (which
# would be inheritance, an "is-a" relationship).
#
# Here, University creates and holds a Department object as one of
# its own attributes. University then delegates to that Department
# object (calling its show_department() method) whenever it needs
# to display department details, instead of duplicating that logic
# itself.
# ============================================================


class Department:
    """Represents a single department, independent of any university."""

    def __init__(self, department_name, head):
        self.department_name = department_name
        self.head = head

    def show_department(self):
        print(f"Department: {self.department_name}")
        print(f"Head of Department: {self.head}")


class University:
    """A University is composed of a Department (has-a relationship)."""

    def __init__(self, university_name, department_name, head):
        self.university_name = university_name
        # The Department object is created and owned by University here.
        # University does not inherit from Department -- it simply holds
        # one as an attribute, which is the essence of composition.
        self.department = Department(department_name, head)

    def show_university(self):
        print(f"University: {self.university_name}")
        # Delegating to the Department object's own method rather than
        # University knowing/duplicating how department details are shown.
        self.department.show_department()


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
# __name__ == "__main__" means: only run this block when the file is
# executed directly (e.g. "python main.py"), not when it is imported
# as a module into another file.
if __name__ == "__main__":
    university = University(
        university_name="Yoobee Colleges",
        department_name="Computer Science",
        head="Dr. Jane Smith",
    )

    print("---- University Details ----")
    university.show_university()
