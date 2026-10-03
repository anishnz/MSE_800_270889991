# ============================================================
# Part F support file: shop.py (before the TDD challenge)
# ============================================================
#
# Same calculate_price()/Product/Inventory as the earlier parts - see
# WK10/ACT_10_8/shop.py. shipping_cost() (at the bottom of this file)
# was added only AFTER test_shipping.py's tests were written and
# watched to fail first (the TDD "red" step) - see
# QUESTION_AND_ANSWER.txt for that failing run.
# ============================================================

import math


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


def shipping_cost(weight_kg):
    """Return the shipping cost for a parcel weighing `weight_kg`:
    $5.00 flat for the first kilogram, plus $2.50 for every additional
    kilogram (any part of a kilogram rounds UP), capped at $25.00."""
    if weight_kg <= 0:
        raise ValueError(f"Weight must be positive, got {weight_kg}.")

    if weight_kg <= 1:
        cost = 5.00
    else:
        extra_kg = math.ceil(weight_kg - 1)
        cost = 5.00 + extra_kg * 2.50

    return min(cost, 25.00)
