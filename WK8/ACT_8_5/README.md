# Travel Package Using the Builder Pattern

## Problem Statement

A travel company allows customers to customise a travel package. A
package can include:

- Destination: Auckland, Sydney, Melbourne, etc.
- Hotel: 3-star, 4-star, 5-star
- Transport: Flight, Train, Bus
- Meal plan: None, Breakfast, Full Board
- Activities: City Tour, Museum, Adventure Tour
- Insurance: Yes/No

The task is to use the Builder Pattern to construct a travel package
step by step.

## Requirements

1. `TravelPackage` — the product: the complex object being built.
2. `TravelPackageBuilder` — the builder: one method per part, each
   returning `self` so calls can be chained, plus a `build()` method.
3. `TravelDirector` — the director: ready-made package recipes that drive
   a builder.
4. A demonstration that builds packages both through the director and
   directly, step by step.

## How It Works

- Putting six values into one constructor is hard to read and easy to get
  in the wrong order. The builder lets the customer choose one part at a
  time instead.
- `TravelPackageBuilder` has `set_destination()`, `set_hotel()`,
  `set_transport()`, `set_meal_plan()`, `add_activity()` and
  `set_insurance()`. Each stores the choice and returns `self`, which is
  what makes chaining like `.set_hotel("4-star").set_transport("Train")`
  possible.
- Parts the customer skips get a default: meal plan "None", no
  activities, no insurance. Destination, hotel and transport have no
  sensible default, so `build()` raises a `ValueError` if any is missing.
- Hotel, transport, meal plan and activity choices are checked against
  the allowed options, so a value such as "2-star" is rejected at once.
- `build()` creates the finished `TravelPackage` from what was collected.
- `TravelDirector` knows the order and the values for three common
  packages (budget, family, luxury). The builder knows how to build; the
  director knows what to build.

## Running the Program

```bash
python main.py
```

### Expected Output

```
--- Budget package (built by the director) ---
Destination : Auckland
Hotel       : 3-star
Transport   : Bus
Meal plan   : None
Activities  : None
Insurance   : No

--- Family package (built by the director) ---
Destination : Sydney
Hotel       : 4-star
Transport   : Flight
Meal plan   : Breakfast
Activities  : City Tour, Museum
Insurance   : Yes

--- Luxury package (built by the director) ---
Destination : Melbourne
Hotel       : 5-star
Transport   : Flight
Meal plan   : Full Board
Activities  : City Tour, Museum, Adventure Tour
Insurance   : Yes

--- Custom package (built step by step by the customer) ---
Destination : Melbourne
Hotel       : 4-star
Transport   : Train
Meal plan   : Full Board
Activities  : Adventure Tour
Insurance   : Yes

--- Invalid choice is rejected ---
Error: Invalid hotel '2-star'. Choose from: 3-star, 4-star, 5-star
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
