# ATM System Using Abstraction

## Problem Statement

A bank wants to develop a simple ATM system. Customers should be able to
perform basic operations such as:

- Insert their card
- Enter their PIN
- Check their balance
- Withdraw money

The customer should only need to know what operation to perform, without
knowing the internal details of how the ATM communicates with the bank's
database or verifies the transaction.

## Requirements

1. Create an abstract class called `ATM`.
2. Define the following abstract methods:
   - `insert_card()`
   - `enter_pin()`
   - `check_balance()`
   - `withdraw(amount)`
3. Create a `BankATM` class that inherits from `ATM`.
4. Implement all the abstract methods in `BankATM`.
5. Create an object of `BankATM` and perform the operations.

## How It Works

- `ATM` is built on Python's `abc.ABC` / `abc.abstractmethod`, so it defines
  *what* operations exist without saying *how* they work, and it cannot be
  instantiated directly.
- `BankATM` **inherits** from `ATM` and provides the real implementation for
  every abstract method, including the internal details the customer never
  sees: verifying the PIN, checking authentication, and updating the
  balance.
- Calling code only ever calls `insert_card()`, `enter_pin()`,
  `check_balance()`, and `withdraw()` — this is **abstraction**: the
  complexity is hidden behind a simple, essential interface.

## Running the Program

```bash
python main.py
```

### Expected Output

```
---- ATM Session ----
Card ending in 1234 inserted.
PIN correct. Access granted.
Current balance: $500.00
Please take your cash: $150.00
Remaining balance: $350.00
Current balance: $350.00
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `question.txt` | The original exercise question |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
