# Payment System Using Polymorphism

## Problem Statement

A company wants to develop a simple payment system. Customers can pay using
different payment methods:

- Credit Card
- PayPal
- Bank Transfer

Each payment method should have a `make_payment()` method, but the way the
payment is processed is different for each method.

The task is to use polymorphism to design this payment system.

## Requirements

Create the following classes:

1. `CreditCard`
2. `PayPal`
3. `BankTransfer`

Each class implements its own `make_payment()` method.

## How It Works

- A common `Payment` base class defines the shared interface
  (`make_payment()`) and stores the shared `amount` attribute.
- `CreditCard`, `PayPal`, and `BankTransfer` each **inherit** from
  `Payment` and **override** `make_payment()` with their own behaviour.
- Because every class shares the same method name, a single loop can call
  `make_payment()` on a list of mixed payment objects without knowing (or
  caring) which specific class each object is — this is **polymorphism**.

## Running the Program

```bash
python main.py
```

### Expected Output

```
---- Processing All Payments ----
Processing credit card payment of $150.00 using card ending in 1234.
Processing PayPal payment of $75.50 via account customer@example.com.
Processing bank transfer of $500.00 to account 12-3456-7890123-00.
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
