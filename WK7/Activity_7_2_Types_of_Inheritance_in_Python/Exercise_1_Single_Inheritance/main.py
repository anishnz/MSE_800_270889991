# ============================================================
# Exercise 1 - Employee Management System
# ============================================================
#
# DEFINITION: Single Inheritance
# -------------------------------
# Single inheritance is a type of inheritance where a CHILD class
# inherits from EXACTLY ONE PARENT (base) class.
#           Employee   <-- parent class
#               |
#           Manager    <-- child class (inherits from Employee ONLY)
#
# Here, "Manager" is a special kind of "Employee", so Manager
# inherits the name and employee_id behaviour from Employee and
# adds its own extra attribute (department).
# ============================================================


class Employee:
    """Parent (base) class representing a general employee."""

    def __init__(self, name, employee_id):
        # self.name and self.employee_id are INSTANCE ATTRIBUTES.
        # They belong to whichever object (self) is being created.
        self.name = name
        self.employee_id = employee_id

    def display_details(self):
        # A regular METHOD that prints out the object's information.
        # Any class that inherits from Employee can reuse this method
        # instead of rewriting the same print statements again.
        print(f"Employee Name : {self.name}")
        print(f"Employee ID   : {self.employee_id}")


class Manager(Employee):
    # The parentheses "(Employee)" is what creates the INHERITANCE.
    # Manager is now a SUBCLASS (child) of Employee, the SUPERCLASS (parent).

    def __init__(self, name, employee_id, department):
        # super() gives access to the parent class (Employee).
        # Calling super().__init__(...) runs Employee's constructor
        # first, so name and employee_id are set up correctly
        # WITHOUT duplicating that code inside Manager.
        super().__init__(name, employee_id)

        # department is a NEW attribute that only Manager has,
        # it does not exist in the base Employee class.
        self.department = department

    def display_details(self):
        # This is METHOD OVERRIDING: Manager provides its OWN version
        # of display_details() instead of just using Employee's version.
        super().display_details()  # reuse the parent's printing logic first
        print(f"Department    : {self.department}")  # then add the extra info


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
if __name__ == "__main__":
    # Creating a Manager object automatically calls Manager.__init__,
    # which in turn calls Employee.__init__ via super().
    manager1 = Manager("Alice Johnson", "EMP1001", "Human Resources")

    print("---- Manager Details ----")
    manager1.display_details()

    # isinstance() confirms the inheritance relationship at runtime:
    print("\nIs manager1 an Employee?", isinstance(manager1, Employee))  # True
    print("Is manager1 a Manager?", isinstance(manager1, Manager))       # True
