# ============================================================
# EMPLOYEE ACCESS MANAGEMENT SYSTEM
# ============================================================

from functools import wraps


# ------------------------------------------------------------
# 1. LOGIN STATUS
# ------------------------------------------------------------

# This variable stores whether the employee is logged in.
# True  = employee is logged in
# False = employee is not logged in
logged_in = True


# ------------------------------------------------------------
# 2. LOGIN REQUIRED DECORATOR
# ------------------------------------------------------------

def login_required(function):
    """
    This decorator checks whether the employee is logged in.
    If logged in -> original function will execute.
    If not logged in -> Access Denied message is displayed.
    """

    # --------------------------------------------------------
    # NESTED FUNCTION
    # --------------------------------------------------------
    # wrapper() is a function INSIDE login_required().
    # This is called a nested function.
    def wrapper():

        # Check the employee's login status.
        if logged_in:

            # Employee is logged in.
            # Therefore, execute the original function.
            return function()

        else:

            # Employee is not logged in.
            # Do NOT execute the original function.
            print("Access Denied: Please log in first.")

    # Return the wrapper function.
    return wrapper


# ------------------------------------------------------------
# 3. EMPLOYEE FUNCTIONS
# ------------------------------------------------------------

@login_required
def view_salary():

    # This message is displayed only if the employee is logged in.
    print("Salary: NZD 5,000 per month")


@login_required
def view_personal_details():

    # This message is displayed only if the employee is logged in.
    print("Personal Details: Name = Anish, Department = IT")


@login_required
def download_report():

    # This message is displayed only if the employee is logged in.
    print("Employee report downloaded successfully.")


# ------------------------------------------------------------
# 4. LIST OF EMPLOYEE FUNCTIONS
# ------------------------------------------------------------

# We store the three functions inside a list.
employee_functions = [
    view_salary,
    view_personal_details,
    download_report
]


# ------------------------------------------------------------
# 5. NESTED LOOP
# ------------------------------------------------------------

# Outer loop:
# Goes through employees.
for employee in ["Employee 1", "Employee 2"]:

    # Display the employee name.
    print("\nEmployee:", employee)

    # Inner loop:
    # Goes through every protected function.
    for function in employee_functions:

        # Display which function is being accessed.
        print("Accessing:", function.__name__)

        # Execute the function.
        function()