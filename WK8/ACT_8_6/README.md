# Car Customisation Using the Decorator Pattern

## Problem Statement

A car company has a basic car:

- Basic Car: $25,000

Customers can optionally add:

- GPS: +$500
- Sunroof: +$1,000
- Leather Seats: +$1,500
- Premium Sound System: +$800

The company does not want separate classes such as `CarWithGPS`,
`CarWithGPSAndSunroof`, `CarWithGPSSunroofAndLeather`, and so on. The task
is to use the Decorator Pattern so that customers can add features
dynamically.

## Requirements

1. `Car` — the component: the interface every car and decorator shares
   (`get_description()` and `get_cost()`).
2. `BasicCar` — the concrete component: the plain $25,000 car.
3. `CarDecorator` — the base decorator: a `Car` that wraps another `Car`.
4. `GPSDecorator`, `SunroofDecorator`, `LeatherSeatsDecorator`,
   `PremiumSoundDecorator` — one concrete decorator per optional feature.
5. A demonstration that stacks features in different combinations.

## How It Works

- With four optional features there are 16 possible combinations. One
  class per combination would mean 16 classes, and each new feature would
  double that. Decorators need only one class per feature.
- A decorator **is a** `Car` (it extends `Car`, so it can be used anywhere a
  car is expected) and **has a** `Car` (the one it wraps, stored in
  `self._car`).
- Each decorator asks the wrapped car for its description and cost, then
  adds its own feature name and price.
- Decorators are stacked by wrapping one around another:

  ```python
  car = SunroofDecorator(GPSDecorator(BasicCar()))
  # description: Basic Car, GPS, Sunroof
  # cost: 25,000 + 500 + 1,000 = 26,500
  ```

- Features are chosen at run time, so a customer can add them one at a
  time: `car = LeatherSeatsDecorator(car)`.
- Because each decorator only adds its own price, the order of stacking
  does not change the total cost.
- Adding a new feature later means adding one new decorator class. No
  existing class is changed.

## Running the Program

```bash
python main.py
```

### Expected Output

```
--- Basic car (no features) ---
Car  : Basic Car
Cost : $25,000

--- Basic car + GPS ---
Car  : Basic Car, GPS
Cost : $25,500

--- Basic car + GPS + Sunroof ---
Car  : Basic Car, GPS, Sunroof
Cost : $26,500

--- Fully loaded car (all four features) ---
Car  : Basic Car, GPS, Sunroof, Leather Seats, Premium Sound System
Cost : $28,800

--- Customer adds features step by step ---
Start          -> $25,000
+ Leather Seats -> $26,500
+ Premium Sound -> $27,300
Car  : Basic Car, Leather Seats, Premium Sound System
Cost : $27,300

--- Order of decorators does not change the cost ---
GPS then Sunroof : $26,500
Sunroof then GPS : $26,500
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
