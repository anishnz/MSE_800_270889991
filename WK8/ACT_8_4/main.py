# ============================================================
# Exercise 2.1: University Configuration Manager (Singleton Pattern)
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. Many parts of the application need the SAME university settings
#      (name, academic year, semester). If each part made its own copy,
#      the copies could disagree with each other.
#   2. So UniversityConfig may only ever have ONE object. The first time
#      we write UniversityConfig(), a real object is created. Every time
#      after that, we get the SAME object back.
#   3. Python calls __new__() BEFORE __init__() to build the object, so
#      __new__() is the right place to decide "create it, or reuse the
#      one that already exists?".
#   4. The one instance is stored in a class variable (_instance). The
#      settings are also given their starting values inside __new__(),
#      so a later UniversityConfig() call cannot wipe them out.
#
# WHY BOTHER? A change made through one object (set_config) is instantly
# visible through every other object, because they are all the same
# object. The `is` operator proves it.
# ============================================================


class UniversityConfig:
    # Holds the one and only instance. None means "not created yet".
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # First call: really create the object and set default values.
            cls._instance = super().__new__(cls)
            cls._instance.university_name = None
            cls._instance.academic_year = None
            cls._instance.semester = None
        # Every call (first or later) returns the same object.
        return cls._instance

    def set_config(self, university_name, academic_year, semester):
        self.university_name = university_name
        self.academic_year = academic_year
        self.semester = semester

    def display_config(self):
        print(f"University Name : {self.university_name}")
        print(f"Academic Year   : {self.academic_year}")
        print(f"Semester        : {self.semester}")


# ==========================================
# Demonstration
# ==========================================
if __name__ == "__main__":
    # Task 4: create three objects.
    config1 = UniversityConfig()
    config2 = UniversityConfig()
    config3 = UniversityConfig()

    # Task 5: set the configuration using the first object.
    config1.set_config("Yoobee College of Creative Innovation", "2026", "Semester 1")

    # Task 6: display the configuration using a different object.
    print("--- Configuration shown through config2 ---")
    config2.display_config()

    # Task 7: verify all three are the same instance with `is`.
    print("\n--- Same instance check ---")
    print("config1 is config2:", config1 is config2)
    print("config2 is config3:", config2 is config3)
    print("config1 is config3:", config1 is config3)

    # Extra: a change through config3 is visible through config1.
    config3.set_config("Yoobee College of Creative Innovation", "2026", "Semester 2")
    print("\n--- After changing the semester through config3, shown via config1 ---")
    config1.display_config()
