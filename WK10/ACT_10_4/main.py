# ============================================================
# Part C: Working with Files
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. read_first_line(path) opens the file with `with open(...) as
#      file:`. `with` guarantees the file is closed when the block
#      ends, EVEN if an exception happens inside it - there is no way
#      to forget to close it.
#   2. file.readline() reads only the first line, including its "\n".
#      .rstrip("\n") removes just that trailing newline so the caller
#      gets a clean string.
#   3. If the path does not exist, Python raises FileNotFoundError
#      before the `with` block's body can run at all. That is caught,
#      a helpful message is printed, and None is returned.
#   4. If the path exists but cannot be read (no permission - on this
#      Windows machine, trying to open a DIRECTORY with open() also
#      raises PermissionError), that is caught separately with its own
#      message, and None is returned.
#   5. EXTENSION - read_first_line_strict() does the same job, but
#      instead of printing it uses `raise DataFileError(...) from error`.
#      This wraps the original FileNotFoundError/PermissionError inside
#      a new, custom exception, while keeping the original attached as
#      `__cause__` (visible in the traceback as "The above exception was
#      the direct cause of the following exception"). The CALLER
#      decides what to print, not the function.
# ============================================================

import os


class DataFileError(Exception):
    """Raised by read_first_line_strict() when a data file cannot be
    read; the original OSError is attached via `raise ... from`."""


def read_first_line(path):
    """Return the first line of a text file (without the trailing
    newline), or None (after printing a message) if it cannot be read."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readline().rstrip("\n")
    except FileNotFoundError:
        print(f"Could not find the file: {path}")
        return None
    except PermissionError:
        print(f"Do not have permission to read the file: {path}")
        return None


def read_first_line_strict(path):
    """Same job as read_first_line(), but raises DataFileError instead
    of printing, so the caller decides how to react."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readline().rstrip("\n")
    except FileNotFoundError as error:
        raise DataFileError(f"Could not find the file: {path}") from error
    except PermissionError as error:
        raise DataFileError(f"Do not have permission to read the file: {path}") from error


if __name__ == "__main__":
    sample_path = "sample.txt"
    missing_path = "does_not_exist.txt"
    directory_path = os.path.dirname(os.path.abspath(__file__))  # a real directory, not a file

    # Make sure the sample file exists, so this demo is repeatable.
    with open(sample_path, "w", encoding="utf-8") as sample_file:
        sample_file.write("Hello from the first line\nsecond line\n")

    print("--- Reading an existing file ---")
    print(repr(read_first_line(sample_path)))

    print("\n--- Reading a file that does not exist ---")
    print(repr(read_first_line(missing_path)))

    print("\n--- Reading a directory instead of a file (raises PermissionError) ---")
    print(repr(read_first_line(directory_path)))

    print("\n--- Extension: read_first_line_strict() raises DataFileError ---")
    try:
        read_first_line_strict(missing_path)
    except DataFileError as error:
        print(f"Caught DataFileError: {error}")
        print(f"Original cause: {type(error.__cause__).__name__}: {error.__cause__}")
