# ============================================================
# Exercise: Food Ordering System Using Factory Design Pattern
# ============================================================
#
# DEFINITION: Factory Design Pattern
# -----------------------------------
# The Factory Pattern provides a way to create objects without the
# calling code needing to know which concrete class is being
# instantiated. Instead of the customer writing `Pizza()`, `Burger()`
# or `Pasta()` directly, they ask a factory for "pizza" and the
# factory decides which class to instantiate and hands back the
# object. This decouples the client from the concrete classes and
# makes it easy to add new food items later without changing any
# client code.
# ============================================================


class Food:
    """Base class for all food items. Defines the common interface."""

    def prepare(self):
        raise NotImplementedError("Subclasses must implement prepare()")


class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza: stretching dough, adding toppings, baking in oven.")


class Burger(Food):
    def prepare(self):
        print("Preparing Burger: grilling patty, toasting bun, adding condiments.")


class Pasta(Food):
    def prepare(self):
        print("Preparing Pasta: boiling pasta, tossing in sauce, plating.")


class FoodFactory:
    """Factory that creates food objects without exposing the concrete classes to the customer."""

    _menu = {
        "pizza": Pizza,
        "burger": Burger,
        "pasta": Pasta,
    }

    @staticmethod
    def create_food(food_type):
        food_class = FoodFactory._menu.get(food_type.lower())
        if food_class is None:
            raise ValueError(f"Unknown food item: {food_type}")
        return food_class()


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
# __name__ == "__main__" means: only run this block when the file is
# executed directly (e.g. "python main.py"), not when it is imported
# as a module into another file.
if __name__ == "__main__":
    orders = ["pizza", "burger", "pasta"]

    for item in orders:
        food = FoodFactory.create_food(item)
        food.prepare()
