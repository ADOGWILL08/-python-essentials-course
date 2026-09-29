# exception_demo.py
# Lab 4 - Part 3: Exception handling with a custom raise, try/except/finally,
# and catching a generic exception


def safe_divide(a, b):
    """
    Divides a by b safely.

    Parameters:
        a (float): the number to divide
        b (float): the number to divide by
    Returns:
        The result of a / b.
    Raises:
        ValueError: if b is zero, since dividing by zero is not allowed.
    """
    if b == 0:
        # We raise our own error on purpose, with a clear custom message,
        # instead of waiting for Python to raise ZeroDivisionError.
        raise ValueError("Cannot divide by zero")
    return a / b


# ---------------- Demonstrate safe_divide with try/except/finally ----------------

# Test values: one normal division, one that will trigger the zero-divisor error
test_pairs = [(10, 2), (5, 0)]

for a, b in test_pairs:
    try:
        result = safe_divide(a, b)
        print(f"{a} / {b} = {result}")
    except ValueError as e:
        # This runs when safe_divide raised our custom ValueError
        print(f"Error: {e}")
    finally:
        # This runs every time, whether or not an error occurred
        print("Division operation completed")


# ---------------- Demonstrate catching a generic Exception ----------------

print("\nNow demonstrating a generic exception:")

unsafe_value = "not_a_number"

try:
    # int() cannot convert this text to a number, so this line raises an error
    converted = int(unsafe_value)
    print(f"Converted value: {converted}")
except Exception as e:
    # Exception is the general category almost all errors belong to.
    # This is a safety net for errors we didn't specifically plan for.
    print(f"An unexpected error occurred: {e}")
finally:
    print("Conversion attempt completed")