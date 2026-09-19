# ============================================================
# Exercise 6 - Custom System: Online Shopping Platform
# ============================================================
#
# System chosen: an ONLINE SHOPPING SYSTEM.
#
# It contains 5 classes and demonstrates TWO different types of
# inheritance combined together (which is itself the definition of
# HYBRID INHERITANCE):
#
#   1) HIERARCHICAL inheritance -> Customer AND Employee both
#      inherit from the same parent class, Person.
#   2) MULTILEVEL inheritance   -> Manager inherits from Employee,
#      which itself inherits from Person (3-level chain).
#
# CLASS DIAGRAM
# --------------
#
#                       Person
#                    (name, email)
#                   /             \
#                  /               \
#            Customer             Employee
#         (customer_id,         (employee_id,
#          loyalty_points)        salary)
#                                     |
#                                     |
#                                  Manager
#                              (department,
#                             team_size)
#
#   - Customer and Employee share one parent (Person) -> HIERARCHICAL
#   - Manager extends Employee which extends Person    -> MULTILEVEL
#   - Together: HYBRID inheritance
# ============================================================


class Person:
    """
    Base class for everyone who interacts with the shopping platform,
    whether they are a customer or a staff member.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_details(self):
        print(f"Name          : {self.name}")
        print(f"Email         : {self.email}")


class Customer(Person):
    # HIERARCHICAL branch #1: Customer inherits from Person.

    def __init__(self, name, email, customer_id, loyalty_points=0):
        super().__init__(name, email)  # set up shared Person fields
        self.customer_id = customer_id
        self.loyalty_points = loyalty_points

    def display_details(self):
        super().display_details()
        print(f"Customer ID   : {self.customer_id}")
        print(f"Loyalty Points: {self.loyalty_points}")

    def earn_points(self, amount_spent):
        # A method unique to Customer: 1 point earned per $10 spent.
        earned = int(amount_spent // 10)
        self.loyalty_points += earned
        print(f"{self.name} earned {earned} loyalty point(s) "
              f"from spending ${amount_spent:.2f}.")


class Employee(Person):
    # HIERARCHICAL branch #2: Employee ALSO inherits from Person.
    # (Customer and Employee sharing the same parent = hierarchical)

    def __init__(self, name, email, employee_id, salary):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Employee ID   : {self.employee_id}")
        print(f"Salary        : ${self.salary:.2f}")


class Manager(Employee):
    # MULTILEVEL continuation: Manager inherits from Employee, which
    # already inherits from Person, forming the chain:
    #       Person -> Employee -> Manager
    # Combined with the Customer/Employee split above, this makes the
    # overall design HYBRID inheritance.

    def __init__(self, name, email, employee_id, salary, department, team_size):
        # super() calls Employee.__init__, which internally calls
        # Person.__init__, so every level gets initialised in order.
        super().__init__(name, email, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display_details(self):
        super().display_details()              # runs Employee -> Person chain
        print(f"Department    : {self.department}")
        print(f"Team Size     : {self.team_size}")

    def give_bonus(self, amount):
        # A method unique to Manager, showing a manager-specific action.
        self.salary += amount
        print(f"{self.name} approved a bonus, new salary: ${self.salary:.2f}")


class Order:
    """
    A supporting class (not part of the Person hierarchy) that ties a
    Customer to a purchase, showing how classes COLLABORATE rather
    than only inherit from one another.
    """

    def __init__(self, order_id, customer: Customer, amount):
        self.order_id = order_id
        self.customer = customer
        self.amount = amount

    def checkout(self):
        print(f"\nProcessing Order {self.order_id} for {self.customer.name} "
              f"- Amount: ${self.amount:.2f}")
        # Reuses a method defined on the Customer object passed in.
        self.customer.earn_points(self.amount)


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
if __name__ == "__main__":
    customer = Customer(
        name="Nabin Adhikari",
        email="nabin.a@example.com",
        customer_id="CUST7001",
        loyalty_points=15,
    )

    manager = Manager(
        name="Sarita Koirala",
        email="sarita.k@shop.com",
        employee_id="EMP9001",
        salary=55000,
        department="Warehouse Operations",
        team_size=12,
    )

    print("---- Customer ----")
    customer.display_details()

    print("\n---- Manager (Hybrid Inheritance: Person -> Employee -> Manager) ----")
    manager.display_details()

    # Demonstrate collaboration + inherited behaviour together:
    order = Order(order_id="ORD00123", customer=customer, amount=249.90)
    order.checkout()
    manager.give_bonus(2000)

    print("\n---- Inheritance relationship checks ----")
    print("Is customer a Person?", isinstance(customer, Person))   # True
    print("Is manager a Person? ", isinstance(manager, Person))    # True (via Employee)
    print("Is manager an Employee?", isinstance(manager, Employee))  # True
    print("Is customer an Employee?", isinstance(customer, Employee))  # False (different branch)
