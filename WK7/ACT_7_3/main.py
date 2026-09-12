# ============================================================
# Exercise: Payment System Using Polymorphism
# ============================================================
#
# DEFINITION: Polymorphism
# -----------------------------------
# Polymorphism means "many forms". Here, every payment class defines
# a make_payment() method with the SAME name, but each class provides
# its OWN implementation of what happens inside that method.
#
#     CreditCard.make_payment()      -> processes a credit card payment
#     PayPal.make_payment()          -> processes a PayPal payment
#     BankTransfer.make_payment()    -> processes a bank transfer
#
# Calling code can treat all payment methods the same way (just call
# make_payment()) without needing to know which specific class it is
# dealing with. This is achieved here through duck typing (all classes
# share the same method name) as well as a common Payment base class.
#
# DEFINITION: Inheritance
# -----------------------------------
# CreditCard, PayPal and BankTransfer all inherit from Payment. This
# means they automatically get Payment's __init__ (which stores the
# amount) and only need to add what is specific to them.
#
# DEFINITION: Method Overriding
# -----------------------------------
# Each subclass defines its own make_payment(), which REPLACES
# (overrides) the version defined in the Payment base class.
# ============================================================


class Payment:
    """Base class defining the common interface for all payment methods."""

    # __init__ is the constructor: it runs automatically whenever a new
    # object is created, and is used to set up the object's starting data.
    def __init__(self, amount):
        # self refers to the specific object being created.
        # self.amount stores the payment amount on that object so every
        # method in the class (and any subclass) can access it later.
        self.amount = amount

    def make_payment(self):
        # This is a placeholder implementation. It exists only so that
        # Payment defines the make_payment() interface that every
        # subclass is expected to override with real behaviour.
        # If a subclass forgets to override it, calling make_payment()
        # will raise this error instead of silently doing nothing.
        raise NotImplementedError("Subclasses must implement make_payment()")


class CreditCard(Payment):  # CreditCard inherits from Payment
    def __init__(self, amount, card_number):
        # super() gives access to the parent class (Payment).
        # This line runs Payment's __init__ so self.amount gets set,
        # without having to repeat that logic here.
        super().__init__(amount)
        # card_number is an attribute specific to CreditCard only;
        # Payment and the other payment types know nothing about it.
        self.card_number = card_number

    # Overriding make_payment(): this version is specific to CreditCard.
    def make_payment(self):
        # self.card_number[-4:] takes a slice of the last 4 characters
        # of the string, e.g. "4111111111111234" -> "1234".
        # This is done so the full card number is never printed/exposed.
        print(f"Processing credit card payment of ${self.amount:.2f} "
              f"using card ending in {self.card_number[-4:]}.")


class PayPal(Payment):  # PayPal inherits from Payment
    def __init__(self, amount, email):
        super().__init__(amount)  # sets self.amount via Payment
        self.email = email        # attribute specific to PayPal only

    # Overriding make_payment(): this version is specific to PayPal.
    def make_payment(self):
        print(f"Processing PayPal payment of ${self.amount:.2f} "
              f"via account {self.email}.")


class BankTransfer(Payment):  # BankTransfer inherits from Payment
    def __init__(self, amount, account_number):
        super().__init__(amount)          # sets self.amount via Payment
        self.account_number = account_number  # specific to BankTransfer

    # Overriding make_payment(): this version is specific to BankTransfer.
    def make_payment(self):
        print(f"Processing bank transfer of ${self.amount:.2f} "
              f"to account {self.account_number}.")


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
# __name__ == "__main__" means: only run this block when the file is
# executed directly (e.g. "python main.py"), not when it is imported
# as a module into another file.
if __name__ == "__main__":
    # A single list holding THREE DIFFERENT types of objects together.
    # This is only possible cleanly because they all share the same
    # make_payment() interface (polymorphism).
    payments = [
        CreditCard(amount=150.00, card_number="4111111111111234"),
        PayPal(amount=75.50, email="customer@example.com"),
        BankTransfer(amount=500.00, account_number="12-3456-7890123-00"),
    ]

    print("---- Processing All Payments ----")
    # Looping through the list, "payment" takes on each object in turn:
    # first a CreditCard, then a PayPal, then a BankTransfer.
    for payment in payments:
        # Same method call, different behaviour depending on the object
        # -- this is polymorphism in action. Python decides at runtime
        # which class's make_payment() to actually run.
        payment.make_payment()
