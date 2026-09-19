# Food Ordering System Using the Factory Pattern

## Problem Statement

A restaurant allows customers to order food using different options:
Pizza, Burger, and Pasta. Each food item has a `prepare()` method.

The task is to use the Factory Design Pattern so a customer can request
a food item without directly creating the corresponding class.

## Requirements

1. `Food` — base class with a `prepare()` method.
2. `Pizza`, `Burger`, `Pasta` — subclasses of `Food`, each implementing
   its own `prepare()`.
3. `FoodFactory` — factory class with `create_food(food_type)` that
   returns the correct food object based on a name string.

## How It Works

- `Food` defines the common interface (`prepare()`) that every food
  item must implement.
- `Pizza`, `Burger`, and `Pasta` each provide their own version of
  `prepare()`.
- `FoodFactory.create_food()` looks up the requested food name in an
  internal menu (`_menu`) and returns a new instance of the matching
  class, or raises a `ValueError` if the name isn't recognized.
- The customer never writes `Pizza()`, `Burger()`, or `Pasta()`
  themselves — they only call `FoodFactory.create_food("pizza")`. This
  decouples the client code from the concrete classes, so new food
  items can be added later by adding a class and a menu entry, with no
  changes needed anywhere the factory is used.

## Running the Program

```bash
python main.py
```

### Expected Output

```
Preparing Pizza: stretching dough, adding toppings, baking in oven.
Preparing Burger: grilling patty, toasting bun, adding condiments.
Preparing Pasta: boiling pasta, tossing in sauce, plating.
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
