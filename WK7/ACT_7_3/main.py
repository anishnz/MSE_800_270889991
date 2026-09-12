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
# ============================================================


class Payment:
    """Base class defining the common interface for all payment methods."""

    def __init__(self, amount):
        self.amount = amount

    def make_payment(self):
        # Each subclass overrides this method with its own behaviour.
        raise NotImplementedError("Subclasses must implement make_payment()")


class CreditCard(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def make_payment(self):
        print(f"Processing credit card payment of ${self.amount:.2f} "
              f"using card ending in {self.card_number[-4:]}.")


class PayPal(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def make_payment(self):
        print(f"Processing PayPal payment of ${self.amount:.2f} "
              f"via account {self.email}.")


class BankTransfer(Payment):
    def __init__(self, amount, account_number):
        super().__init__(amount)
        self.account_number = account_number

    def make_payment(self):
        print(f"Processing bank transfer of ${self.amount:.2f} "
              f"to account {self.account_number}.")


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
if __name__ == "__main__":
    payments = [
        CreditCard(amount=150.00, card_number="4111111111111234"),
        PayPal(amount=75.50, email="customer@example.com"),
        BankTransfer(amount=500.00, account_number="12-3456-7890123-00"),
    ]

    print("---- Processing All Payments ----")
    for payment in payments:
        # Same method call, different behaviour depending on the object
        # -- this is polymorphism in action.
        payment.make_payment()
