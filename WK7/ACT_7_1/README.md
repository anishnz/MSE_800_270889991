# Bank Account Management System

## Problem Statement

A bank wants a simple program to manage customer accounts. Every account
has an account number, a customer name, and a balance, and supports
depositing and withdrawing money. Savings accounts are a special kind of
account that also earns interest.

The task is to model this using inheritance: a general `BankAccount`
class, and a `SavingsAccount` class that reuses `BankAccount`'s behaviour
and adds interest calculation on top of it.

## Requirements

Create the following classes:

1. `BankAccount` - holds `account_number`, `customer_name`, `balance`,
   and provides `display_account_details()`, `deposit()`, and
   `withdraw()`.
2. `SavingsAccount` (inherits from `BankAccount`) - adds
   `calculate_interest()` and overrides `display_account_details()` to
   also show the account type.

## How It Works

- `BankAccount` is the parent (base) class. It stores the shared data
  (account number, customer name, balance) and defines the shared
  behaviour (`display_account_details`, `deposit`, `withdraw`).
- `SavingsAccount` **inherits** from `BankAccount` using
  `class SavingsAccount(BankAccount):`, so it automatically gets the
  constructor, `deposit()`, and `withdraw()` without rewriting them.
  This is **single inheritance** - one child class, one parent class.
- `SavingsAccount` adds a new method, `calculate_interest()`, that is
  specific to savings accounts only.
- `SavingsAccount` also **overrides** `display_account_details()` to
  print "Account Type: Savings Account" first, then calls
  `super().display_account_details()` to reuse the parent's printing
  logic for the rest of the details (this is **method overriding**
  combined with `super()`).
- The demonstration code creates one `SavingsAccount`, then deposits,
  withdraws, and calculates interest on it, printing the account state
  before and after each operation.

Note: unlike the exercises in `Activity_7_2_Types_of_Inheritance_in_Python`,
this script's demonstration code runs directly at module level (there is
no `if __name__ == "__main__":` guard), but it still runs correctly with
`python main.py`.

## Running the Program

```bash
python main.py
```

### Expected Output

```
Initial Account Details
Account Type: Savings Account
Account Number: SA1001
Customer Name: John
Account Balance: $5000.00

After Deposit
Deposited: $1000.00
New Balance: $6000.00

After Withdrawal
Withdrawn: $500.00
New Balance: $5500.00

Interest Calculation
Interest at 5.00%: $275.00

Final Account Details
Account Type: Savings Account
Account Number: SA1001
Customer Name: John
Account Balance: $5500.00
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
