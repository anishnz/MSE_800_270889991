# ============================================================
# Part A: Predict the Output
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   Each snippet below is run through once. Before looking at the
#   PREDICTED line in the comment, read the code and write down what you
#   think it prints - then run this file and compare with the ACTUAL
#   output underneath each prediction.
#
#   The thing every snippet is really testing is ORDER:
#     - try runs first, top to bottom, until something either finishes
#       or raises.
#     - except only runs if a matching exception was raised, and it
#       only sees the exception type(s) it is allowed to catch.
#     - else only runs if NO exception was raised in the try block.
#     - finally ALWAYS runs - whether the try succeeded, an except
#       handled an error, or even if the try block used `return`.
# ============================================================


def a1():
    print("--- A1 ---")
    # PREDICTED: A / C / D
    #   "A" prints, then int("abc") raises ValueError before "B" can
    #   print, so the except block prints "C", and finally always runs
    #   last, printing "D".
    try:
        print("A")
        x = int("abc")
        print("B")
    except ValueError:
        print("C")
    finally:
        print("D")


def a2():
    print("--- A2 ---")
    # PREDICTED: cleanup / try
    #   finally runs BEFORE the function actually hands its return value
    #   back to the caller, so "cleanup" is printed while f() is still
    #   finishing, and only then does print(f()) print the value "try"
    #   that f() returned.
    def f():
        try:
            return "try"
        finally:
            print("cleanup")

    print(f())


def a3():
    print("--- A3 ---")
    # PREDICTED: IndexError
    #   nums[5] is out of range, so IndexError is raised. It matches the
    #   except tuple (IndexError, KeyError), so type(e).__name__ prints
    #   "IndexError". else is skipped because an exception DID happen.
    try:
        nums = [1, 2, 3]
        print(nums[5])
    except (IndexError, KeyError) as e:
        print(type(e).__name__)
    else:
        print("no error")


def a4():
    print("--- A4 ---")
    # PREDICTED: 5.0 / ok
    #   10 / 2 succeeds and prints 5.0, so no exception happens and the
    #   else block runs too, printing "ok".
    try:
        print(10 / 2)
    except ZeroDivisionError:
        print("zero")
    else:
        print("ok")


if __name__ == "__main__":
    a1()
    print()
    a2()
    print()
    a3()
    print()
    a4()
