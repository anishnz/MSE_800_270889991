# University Configuration Manager Using the Singleton Pattern

## Problem Statement

Different parts of a university management system need the same
configuration: university name, academic year and semester. To keep them
consistent, only one `UniversityConfig` object may exist. Every time a new
`UniversityConfig` is created, it must refer to that same instance.

## Requirements

1. Create a `UniversityConfig` class.
2. Implement the Singleton pattern using `__new__()`.
3. Store the university name, academic year and semester.
4. Create three objects from `UniversityConfig`.
5. Set the configuration using one object.
6. Display the configuration using another object.
7. Use `is` to verify that all objects are the same instance.

## How It Works

- `UniversityConfig._instance` is a class variable that starts as `None`.
- `__new__()` runs before `__init__()` and decides what object to return.
  On the first call it creates the object, stores it in `_instance` and
  gives the three settings their starting values. On every later call it
  simply returns the stored object.
- The starting values are set inside `__new__()` (not `__init__()`)
  because `__init__()` runs on every `UniversityConfig()` call and would
  reset the settings each time.
- `set_config()` stores the settings and `display_config()` prints them.
- Because `config1`, `config2` and `config3` are the same object, setting
  the configuration through `config1` and displaying it through `config2`
  shows the same values, and `is` returns `True` for every pair.

## Running the Program

```bash
python main.py
```

### Expected Output

```
--- Configuration shown through config2 ---
University Name : Yoobee College of Creative Innovation
Academic Year   : 2026
Semester        : Semester 2

--- Same instance check ---
config1 is config2: True
config2 is config3: True
config1 is config3: True

--- After changing the semester through config3, shown via config1 ---
University Name : Yoobee College of Creative Innovation
Academic Year   : 2026
Semester        : Semester 3
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definition and demonstration code |
| `README.md` | This file |
