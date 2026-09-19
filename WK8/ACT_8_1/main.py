# ============================================================
# Exercise: Food Ordering System Using Factory Design Pattern
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. Make one class per food item (Pizza, Burger, Pasta). Each one
#      knows how to prepare() itself.
#   2. Make ONE factory class whose only job is: "given a name like
#      'pizza', build and return the matching object."
#   3. The customer only ever talks to the factory. They say what
#      they want as plain text -- they never type `Pizza()` etc.
#      themselves.
#
# WHY BOTHER? If the customer created objects directly (e.g.
# `Pizza()`), they would need to know every class name in the
# program. With a factory, they only need to know one method:
# `FoodFactory.create_food("pizza")`. Adding a new food later means
# adding one class + one line in the factory -- nothing else changes.
# ============================================================


# ------------------------------------------------------------
# STEP 1: Define a common "shape" that every food item follows.
# ------------------------------------------------------------
# Every food item must have a prepare() method. This class exists
# only to describe that rule; it is never used on its own.
class Food:
    def prepare(self):
        raise NotImplementedError("Subclasses must implement prepare()")


# ------------------------------------------------------------
# STEP 2: Create one simple class per food item.
# ------------------------------------------------------------
# Each class inherits from Food and fills in its own prepare() logic.
class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza: stretching dough, adding toppings, baking in oven.")


class Burger(Food):
    def prepare(self):
        print("Preparing Burger: grilling patty, toasting bun, adding condiments.")


class Pasta(Food):
    def prepare(self):
        print("Preparing Pasta: boiling pasta, tossing in sauce, plating.")


# ------------------------------------------------------------
# STEP 3: Build the factory -- the single place that decides which
# class to create, based on the food name the customer typed in.
# ------------------------------------------------------------
class FoodFactory:
    @staticmethod
    def create_food(food_name):
        food_name = food_name.lower()  # so "Pizza" and "pizza" both work

        # Simple if/elif chain: match the name to a class and build it.
        if food_name == "pizza":
            return Pizza()
        elif food_name == "burger":
            return Burger()
        elif food_name == "pasta":
            return Pasta()
        else:
            raise ValueError(f"Unknown food item: {food_name}")


# ------------------------------------------------------------
# STEP 4: Demonstration -- walk through placing three orders.
# ------------------------------------------------------------
# __name__ == "__main__" means: only run this block when the file is
# executed directly (e.g. "python main.py"), not when it is imported
# as a module into another file.
if __name__ == "__main__":
    orders = ["pizza", "burger", "pasta"]

    for order_name in orders:
        print(f"\nCustomer orders: {order_name}")

        # The customer/client code never creates Pizza(), Burger(), or
        # Pasta() itself -- it just hands a name to the factory...
        food_item = FoodFactory.create_food(order_name)

        # ...and gets back a ready-to-use object with a prepare() method.
        food_item.prepare()
