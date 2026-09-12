# ============================================================
# Exercise: ATM System Using Abstraction
# ============================================================
#
# DEFINITION: Abstraction
# -----------------------------------
# Abstraction means exposing only the essential operations a user
# needs (insert_card, enter_pin, check_balance, withdraw) while
# hiding how those operations are actually carried out (talking to
# the bank's database, verifying the PIN, updating the balance).
# The customer only needs to know WHAT the ATM can do, not HOW it
# does it internally.
#
# DEFINITION: Abstract Class / Abstract Method
# -----------------------------------
# ATM is an abstract class: it defines the required operations
# (as abstract methods) but provides no implementation for them.
# Python's abc module enforces this -- ATM cannot be instantiated
# directly, and any subclass MUST implement every abstract method
# or it cannot be instantiated either.
#
# DEFINITION: Inheritance
# -----------------------------------
# BankATM inherits from ATM, meaning it must fulfil the contract
# defined by ATM by implementing all four abstract methods.
# ============================================================

from abc import ABC, abstractmethod


class ATM(ABC):
    """Abstract class defining the essential operations an ATM must provide."""

    # @abstractmethod marks a method that has no implementation here.
    # Any subclass of ATM must override every one of these methods,
    # otherwise Python will refuse to create an instance of that subclass.
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self, pin):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class BankATM(ATM):  # BankATM inherits from ATM and implements its contract
    def __init__(self, card_number, correct_pin, balance):
        # These attributes represent the internal state that the customer
        # never has to know about directly -- they only call the methods.
        self.card_number = card_number
        self._correct_pin = correct_pin
        self._balance = balance
        self._card_inserted = False
        self._authenticated = False

    def insert_card(self):
        # Hides the internal detail of "reading" the card from the machine.
        self._card_inserted = True
        print(f"Card ending in {self.card_number[-4:]} inserted.")

    def enter_pin(self, pin):
        # Hides how the PIN is actually verified against the bank's records.
        if not self._card_inserted:
            print("Please insert your card first.")
            return

        if pin == self._correct_pin:
            self._authenticated = True
            print("PIN correct. Access granted.")
        else:
            self._authenticated = False
            print("Incorrect PIN. Access denied.")

    def check_balance(self):
        # The customer just asks for the balance; they don't know (or need
        # to know) that this method is guarding access with authentication.
        if not self._authenticated:
            print("Cannot check balance: please insert card and enter the correct PIN.")
            return

        print(f"Current balance: ${self._balance:.2f}")

    def withdraw(self, amount):
        # Hides the internal validation (authentication, funds check) and
        # the internal update of the balance behind a single simple call.
        if not self._authenticated:
            print("Cannot withdraw: please insert card and enter the correct PIN.")
            return

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self._balance:
            print(f"Insufficient funds. Available balance: ${self._balance:.2f}")
            return

        self._balance -= amount
        print(f"Please take your cash: ${amount:.2f}")
        print(f"Remaining balance: ${self._balance:.2f}")


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
# __name__ == "__main__" means: only run this block when the file is
# executed directly (e.g. "python main.py"), not when it is imported
# as a module into another file.
if __name__ == "__main__":
    # The customer only interacts through insert_card / enter_pin /
    # check_balance / withdraw -- none of the internal bank logic above
    # is visible from here. That is abstraction in action.
    atm = BankATM(card_number="4111111111111234", correct_pin="1234", balance=500.00)

    print("---- ATM Session ----")
    atm.insert_card()
    atm.enter_pin("1234")
    atm.check_balance()
    atm.withdraw(150.00)
    atm.check_balance()
