# Operating System UI Factory Using the Abstract Factory Pattern

## Problem Statement

An application must work on different operating systems. Each operating
system has its own matching set of UI components:

- Windows → Windows Button + Windows Checkbox
- Mac → Mac Button + Mac Checkbox

The task is to use the Abstract Factory Pattern so that each factory
creates a matching family of UI components, and the client works without
knowing which operating system is being used.

## Requirements

1. `Button` — abstract product with an abstract `click()` method.
2. `Checkbox` — abstract product with an abstract `check()` method.
3. `WindowsButton`, `WindowsCheckbox`, `MacButton`, `MacCheckbox` —
   concrete products.
4. `GUIFactory` — abstract factory with `create_button()` and
   `create_checkbox()`.
5. `WindowsFactory`, `MacFactory` — concrete factories, each creating
   one matching family.
6. A client (`Application`) that uses only the abstract factory and the
   abstract products.

## How It Works

- `Button` and `Checkbox` are rule books: every button must have
  `click()` and every checkbox must have `check()`. They are abstract, so
  they cannot be created directly.
- The Windows classes and the Mac classes each provide their own version
  of those methods. Together the Windows button and checkbox form one
  family, and the Mac button and checkbox form another.
- `GUIFactory` is the rule book for factories: every factory must be
  able to create a button **and** a checkbox.
- `WindowsFactory` and `MacFactory` each create one whole family. They
  are the only place the concrete product classes are instantiated, so
  a Windows button can never be mixed with a Mac checkbox.
- `Application` (the client) receives a factory, asks it for a button
  and a checkbox, then calls `click()` and `check()`. It never mentions
  Windows or Mac. To add a new OS (for example Linux), add two product
  classes and one factory; existing code stays untouched.

### Factory Method vs Abstract Factory

| Factory Method (ACT_8_2) | Abstract Factory (this exercise) |
|---|---|
| One factory creates **one** type of product | One factory creates a **family** of related products |
| `EmailFactory.create_notification()` | `WindowsFactory.create_button()` and `create_checkbox()` |

## Running the Program

```bash
python main.py
```

### Expected Output

```
--- Windows ---
Clicked a Windows Button
Checked a Windows Checkbox

--- Mac ---
Clicked a Mac Button
Checked a Mac Checkbox

--- Detected operating system: Windows ---
Clicked a Windows Button
Checked a Windows Checkbox
```

The last block depends on the machine: on Mac it prints `Darwin` and the
Mac components, and on any other OS it reports that no factory is
available.

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
