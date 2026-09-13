# ============================================================
# Exercise 3 - University Employee Types
# ============================================================
#
# DEFINITION: Hierarchical Inheritance
# --------------------------------------
# Hierarchical inheritance is a type of inheritance where MORE THAN
# ONE child class inherits from the SAME single parent class.
#
#                       Employee                <-- one parent
#              /            |            \
#        Lecturer     Administrator    Technician   <-- many children
#
# Each child class shares the common attributes/methods of Employee,
# but also defines its OWN unique attribute.
# ============================================================


class Employee:
    """Parent class shared by all university employee types."""

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_details(self):
        print(f"Name        : {self.name}")
        print(f"Employee ID : {self.employee_id}")


class Lecturer(Employee):
    # Branch 1 of the hierarchy: Lecturer inherits from Employee.

    def __init__(self, name, employee_id, teaching_subject):
        super().__init__(name, employee_id)  # set up shared Employee fields
        self.teaching_subject = teaching_subject  # unique to Lecturer

    def display_details(self):
        super().display_details()
        print(f"Teaching Subject : {self.teaching_subject}")


class Administrator(Employee):
    # Branch 2 of the hierarchy: Administrator ALSO inherits from Employee.
    # This is what makes it "hierarchical" - multiple classes sharing one parent.

    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department  # unique to Administrator

    def display_details(self):
        super().display_details()
        print(f"Department       : {self.department}")


class Technician(Employee):
    # Branch 3 of the hierarchy: Technician also inherits from Employee.

    def __init__(self, name, employee_id, technical_specialisation):
        super().__init__(name, employee_id)
        self.technical_specialisation = technical_specialisation  # unique field

    def display_details(self):
        super().display_details()
        print(f"Specialisation   : {self.technical_specialisation}")


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
if __name__ == "__main__":
    lecturer = Lecturer("Dr. Sita Rai", "EMP2001", "Data Structures")
    administrator = Administrator("Ramesh Gurung", "EMP2002", "Admissions Office")
    technician = Technician("Hari Thapa", "EMP2003", "Network Systems")

    print("---- Lecturer ----")
    lecturer.display_details()

    print("\n---- Administrator ----")
    administrator.display_details()

    print("\n---- Technician ----")
    technician.display_details()

    # All three are different classes, but all share the same parent (Employee):
    print("\nAll are Employees?",
          isinstance(lecturer, Employee),
          isinstance(administrator, Employee),
          isinstance(technician, Employee))
