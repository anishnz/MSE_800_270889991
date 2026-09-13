# ============================================================
# Exercise 5 - Hospital Staff and Patients
# ============================================================
#
# DEFINITION: Hybrid Inheritance
# ---------------------------------
# Hybrid inheritance is a COMBINATION of two or more types of
# inheritance in a single design. In this exercise we combine:
#
#   1) HIERARCHICAL inheritance -> both Doctor AND Nurse inherit
#      from the same parent, Person.
#   2) MULTILEVEL inheritance   -> SeniorNurse inherits from Nurse,
#      which itself inherits from Person (a 3-level chain).
#
# Putting both together in one design makes this HYBRID inheritance.
#
# CLASS DIAGRAM
# --------------
#
#                    Person
#                 (name)
#                /        \
#               /          \
#          Doctor          Nurse
#       (doctor_id)      (nurse_id)
#                            |
#                            |
#                       SeniorNurse
#                         (ward)
#
#   - Doctor and Nurse both branch off Person   -> HIERARCHICAL part
#   - SeniorNurse branches off Nurse            -> MULTILEVEL part
# ============================================================


class Person:
    """Top-level base class. Every hospital person has a name."""

    def __init__(self, name):
        self.name = name

    def display_details(self):
        print(f"Name       : {self.name}")


class Doctor(Person):
    # HIERARCHICAL branch #1: Doctor inherits from Person.

    def __init__(self, name, doctor_id):
        super().__init__(name)
        self.doctor_id = doctor_id

    def display_details(self):
        super().display_details()
        print(f"Doctor ID  : {self.doctor_id}")


class Nurse(Person):
    # HIERARCHICAL branch #2: Nurse ALSO inherits from Person.
    # (Doctor and Nurse sharing the same parent = hierarchical inheritance)

    def __init__(self, name, nurse_id):
        super().__init__(name)
        self.nurse_id = nurse_id

    def display_details(self):
        super().display_details()
        print(f"Nurse ID   : {self.nurse_id}")


class SeniorNurse(Nurse):
    # MULTILEVEL continuation: SeniorNurse inherits from Nurse, which in
    # turn inherits from Person, forming a 3-level chain:
    #     Person -> Nurse -> SeniorNurse
    # Combined with the Doctor/Nurse split above, the OVERALL design is
    # HYBRID inheritance (hierarchical + multilevel together).

    def __init__(self, name, nurse_id, ward):
        # super() here calls Nurse.__init__, which itself calls
        # Person.__init__, initialising all levels of the chain.
        super().__init__(name, nurse_id)
        self.ward = ward  # extra attribute unique to SeniorNurse

    def display_details(self):
        super().display_details()          # runs Nurse -> Person chain
        print(f"Ward       : {self.ward}")


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
if __name__ == "__main__":
    doctor = Doctor("Dr. Anish Karki", "DOC501")
    nurse = Nurse("Nurse Maya Lama", "NUR301")
    senior_nurse = SeniorNurse("Nurse Sunita Basnet", "NUR105", "Cardiology Ward")

    print("---- Doctor ----")
    doctor.display_details()

    print("\n---- Nurse ----")
    nurse.display_details()

    print("\n---- Senior Nurse (Hybrid Inheritance) ----")
    senior_nurse.display_details()

    print("\nIs senior_nurse a Nurse? ", isinstance(senior_nurse, Nurse))    # True
    print("Is senior_nurse a Person?", isinstance(senior_nurse, Person))   # True
    print("Is senior_nurse a Doctor?", isinstance(senior_nurse, Doctor))   # False (different branch)
