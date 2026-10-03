# ============================================================
# Part A support file: shop.py (the "Section 2" file this exercise
# set builds on)
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. calculate_price(price, quantity, discount=0.0) is the function
#      every later part tests. It validates its three inputs first
#      (price > 0, quantity > 0, 0 <= discount < 1), then returns
#      price * quantity * (1 - discount), rounded to 2 decimal places.
#   2. Product is a tiny record: a name, a price, and how many are in
#      stock.
#   3. Inventory holds many Products by name. sell() reduces stock (or
#      raises ValueError if there isn't enough), and
#      cheapest_in_stock() returns the lowest-priced Product that still
#      has stock > 0 - or None if nothing is left at all.
# ============================================================


def calculate_price(price, quantity, discount=0.0):
    """Return the total price for `quantity` items at `price` each,
    after an optional `discount` (0.0-0.99), rounded to 2 decimals."""
    if price <= 0:
        raise ValueError(f"Price must be positive, got {price}.")
    if quantity <= 0:
        raise ValueError(f"Quantity must be positive, got {quantity}.")
    if discount < 0 or discount >= 1:
        raise ValueError(f"Discount must be between 0 and 1 (exclusive), got {discount}.")

    total = price * quantity * (1 - discount)
    return round(total, 2)


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, name, price, stock):
        self._products[name] = Product(name, price, stock)

    def sell(self, name, quantity):
        if name not in self._products:
            raise ValueError(f"No such product: {name}")

        product = self._products[name]
        if quantity > product.stock:
            raise ValueError(
                f"Not enough {name} in stock: requested {quantity}, have {product.stock}."
            )

        product.stock -= quantity

    def in_stock_products(self):
        return [p for p in self._products.values() if p.stock > 0]

    def cheapest_in_stock(self):
        in_stock = self.in_stock_products()
        if not in_stock:
            return None
        return min(in_stock, key=lambda p: p.price)
