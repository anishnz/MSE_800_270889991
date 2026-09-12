"""Employee Access Management System.

Small demo of a login-gated access control system using a decorator.

- A single global flag (`logged_in`) simulates whether an employee is
  currently logged in.
- `login_required` is a decorator: it wraps any function so that the
  function's real code only runs if `logged_in` is True; otherwise an
  "Access Denied" message is shown instead.
- Three employee-facing functions (`view_salary`, `view_personal_details`,
  `download_report`) are protected with `@login_required`.
- The bottom of the file simulates two employees each accessing all three
  protected functions in turn, to demonstrate the decorator in action.
"""

# ============================================================
# EMPLOYEE ACCESS MANAGEMENT SYSTEM
# ============================================================

# functools.wraps is imported so it could be used to preserve a wrapped
# function's original name/docstring when writing a decorator (see the
# note near login_required() below on how it would normally be applied).
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
    # NOTE: @wraps(function) from functools is not actually applied here
    # (it is only imported at the top of the file). Normally you would
    # decorate wrapper with @wraps(function) so that wrapper.__name__
    # matches the original function's name. Without it, every decorated
    # function's __name__ shows up as "wrapper" (see the nested loop at
    # the bottom of this file, which prints function.__name__).
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

# The "@login_required" line above each function below is decorator
# syntax. Writing "@login_required" directly above "def view_salary():"
# is equivalent to writing:
#     view_salary = login_required(view_salary)
# i.e. the name view_salary now actually refers to the wrapper() function
# returned by login_required(), with the original view_salary logic
# captured inside it as "function".

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

# We store the three functions inside a list. Note these are the
# decorated (wrapper) versions of the functions, since @login_required
# already replaced each name with its wrapper above.
employee_functions = [
    view_salary,
    view_personal_details,
    download_report
]


# ------------------------------------------------------------
# 5. NESTED LOOP
# ------------------------------------------------------------

# Outer loop:
# Goes through employees. This is just a list of two plain strings used
# as display labels - logged_in is a single global flag, so it is not
# tracked per employee here; both "employees" get the same access result.
for employee in ["Employee 1", "Employee 2"]:

    # Display the employee name.
    print("\nEmployee:", employee)

    # Inner loop:
    # Goes through every protected function.
    for function in employee_functions:

        # Display which function is being accessed.
        # (Prints "wrapper" rather than the real function name - see the
        # NOTE above wrapper()'s definition explaining why.)
        print("Accessing:", function.__name__)

        # Execute the function. Because each function in this list is the
        # login_required wrapper, calling it here re-checks logged_in and
        # either runs the original function or prints "Access Denied".
        function()