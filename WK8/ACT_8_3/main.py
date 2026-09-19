# ============================================================
# Exercise 1.5: Operating System UI Factory (Abstract Factory Pattern)
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. Every button must have a click() method and every checkbox must
#      have a check() method. We describe those rules once, in two
#      abstract classes (Button and Checkbox).
#   2. Each operating system gets its OWN button and checkbox classes
#      (WindowsButton + WindowsCheckbox, MacButton + MacCheckbox).
#      Together they form a "family" of matching components.
#   3. Each operating system also gets ONE factory that creates the
#      whole family: WindowsFactory makes Windows parts, MacFactory
#      makes Mac parts.
#   4. The client (the Application class) only talks to a GUIFactory.
#      It never writes WindowsButton() or MacCheckbox() itself.
#
# WHY BOTHER? Because one factory only hands out parts from ONE family,
# a Windows button can never end up next to a Mac checkbox. To support
# a new OS (e.g. Linux) we add two product classes + one factory; the
# client code does not change.
#
# FACTORY METHOD vs ABSTRACT FACTORY:
#   Factory Method  -> one factory creates ONE type of product.
#   Abstract Factory -> one factory creates a FAMILY of related products.
# ============================================================

import platform
from abc import ABC, abstractmethod


# ==========================================
# 1. ABSTRACT PRODUCTS
# ==========================================
# "Product" = a thing the factory makes. There are TWO kinds of product
# here (button and checkbox), so there are TWO abstract product classes.
# Each is a rule book: it says which method every version must have.
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass


# ==========================================
# 2. CONCRETE PRODUCTS -- Windows family
# ==========================================
# "Concrete" = a real, usable class. Each one inherits from an abstract
# product and writes its own version of the method.
class WindowsButton(Button):
    def click(self):
        print("Clicked a Windows Button")


class WindowsCheckbox(Checkbox):
    def check(self):
        print("Checked a Windows Checkbox")


# ==========================================
# 3. CONCRETE PRODUCTS -- Mac family
# ==========================================
class MacButton(Button):
    def click(self):
        print("Clicked a Mac Button")


class MacCheckbox(Checkbox):
    def check(self):
        print("Checked a Mac Checkbox")


# ==========================================
# 4. ABSTRACT FACTORY
# ==========================================
# The rule book for factories: every factory MUST be able to create a
# button AND a checkbox. It does not say WHICH operating system --
# each concrete factory decides that.
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# ==========================================
# 5. CONCRETE FACTORIES
# ==========================================
# One factory per operating system. Each one builds a matching pair:
# both parts come from the same family. These are the ONLY places
# where WindowsButton(), WindowsCheckbox(), MacButton() and
# MacCheckbox() are written.
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


# ==========================================
# 6. CLIENT
# ==========================================
# The client is handed a factory and only uses the abstract methods
# create_button(), create_checkbox(), click() and check(). It never
# mentions Windows or Mac, so it works with any factory.
class Application:
    def __init__(self, factory):
        # Ask the factory for the matching parts.
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def run(self):
        # Same calls no matter which operating system is behind them.
        self.button.click()
        self.checkbox.check()


# ==========================================
# 7. DEMONSTRATION
# ==========================================
# __name__ == "__main__" means: only run this block when the file is
# executed directly (python main.py), not when it is imported.
if __name__ == "__main__":
    # Step A: pick a factory (this decides which family we get).
    # Step B: hand it to the client.
    # Step C: run the client. Only the factory on the first line changes.
    print("--- Windows ---")
    Application(WindowsFactory()).run()

    print("\n--- Mac ---")
    Application(MacFactory()).run()

    # Optional: the factory can also be chosen automatically from the
    # OS the program is really running on. platform.system() returns
    # "Windows" on Windows and "Darwin" on Mac. The client below is the
    # same Application class -- it still does not know which OS it is.
    print("\n--- Detected operating system: " + platform.system() + " ---")
    factories = {"Windows": WindowsFactory, "Darwin": MacFactory}
    factory_class = factories.get(platform.system())
    if factory_class is None:
        print("No UI factory available for this operating system.")
    else:
        Application(factory_class()).run()
