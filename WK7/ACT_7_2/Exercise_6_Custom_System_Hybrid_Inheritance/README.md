# Exercise 6: Custom System - Online Shopping Platform (Hybrid Inheritance)

## Problem Statement

Design a custom system of your choosing that uses at least 5 classes and
demonstrates a combination of inheritance types. This exercise models an
**online shopping platform**: customers and employees are both people who
share a name and email; managers are a special, more senior kind of
employee; and orders tie a customer to a purchase.

## Requirements

Create a system with at least 5 classes, combining two types of
inheritance:

1. `Person` - base class with `name`, `email`, `display_details()`.
2. `Customer` (inherits from `Person`) - adds `customer_id`,
   `loyalty_points`, and `earn_points()`.
3. `Employee` (inherits from `Person`) - adds `employee_id`, `salary`.
4. `Manager` (inherits from `Employee`) - adds `department`,
   `team_size`, and `give_bonus()`.
5. `Order` - a supporting class (not part of the `Person` hierarchy)
   that links a `Customer` to a purchase and calls back into the
   customer's own behaviour.

## How It Works

```
                   Person
                (name, email)
               /             \
              /               \
        Customer             Employee
     (customer_id,         (employee_id,
      loyalty_points)        salary)
                                 |
                                 |
                              Manager
                          (department,
                         team_size)
```

- `Customer` and `Employee` both inherit directly from `Person` -
  **hierarchical inheritance** (two children, one shared parent).
- `Manager` inherits from `Employee`, which inherits from `Person`,
  forming a 3-level chain `Person -> Employee -> Manager` -
  **multilevel inheritance**.
- Combining both patterns in the same design is **hybrid inheritance**.
- `Order` is a separate, unrelated class that **collaborates** with
  `Customer` (it holds a reference to a `Customer` object and calls
  `customer.earn_points(...)` on it) rather than inheriting from it -
  showing that not every relationship between classes needs to be
  inheritance; some are simple object collaboration/composition.
- The demonstration code creates a `Customer` and a `Manager`, displays
  both, places an `Order` for the customer (which awards loyalty
  points), gives the manager a bonus, and finally uses `isinstance()`
  to show that a `Manager` is a `Person` and an `Employee`, but a
  `Customer` is a `Person` and NOT an `Employee` (different branch).

## Running the Program

```bash
python main.py
```

### Expected Output

```
---- Customer ----
Name          : Nabin Adhikari
Email         : nabin.a@example.com
Customer ID   : CUST7001
Loyalty Points: 15

---- Manager (Hybrid Inheritance: Person -> Employee -> Manager) ----
Name          : Sarita Koirala
Email         : sarita.k@shop.com
Employee ID   : EMP9001
Salary        : $55000.00
Department    : Warehouse Operations
Team Size     : 12

Processing Order ORD00123 for Nabin Adhikari - Amount: $249.90
Nabin Adhikari earned 24 loyalty point(s) from spending $249.90.
Sarita Koirala approved a bonus, new salary: $57000.00

---- Inheritance relationship checks ----
Is customer a Person? True
Is manager a Person?  True
Is manager an Employee? True
Is customer an Employee? False
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
