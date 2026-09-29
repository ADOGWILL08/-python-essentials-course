# calc_with_functions.py
# Lab 4 - Part 1: Calculator refactored to use functions and exception handling


def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns a minus b."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


def divide(a, b):
    """
    Returns a divided by b.
    Python raises a ZeroDivisionError if b is 0. We do not catch it here;
    the main program catches it and prints a friendly message.
    """
    return a / b


def calculate(a, b, op):
    """
    Calls the correct operation function based on the operation symbol.

    Parameters:
        a (float): the first number
        b (float): the second number
        op (str): the operation symbol: +, -, *, or /
    Returns:
        The result of the operation, or None if the symbol is invalid.
    """
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        # Invalid operation symbol: print an error and return None
        print(f"Error: '{op}' is not a valid operation. Use +, -, * or /.")
        return None


# ---------------- Main program ----------------

try:
    # float() converts the typed text into a number.
    # If the text is not a number (like "abc"), Python raises a ValueError.
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ").strip()

    # calculate() may raise ZeroDivisionError when dividing by zero
    result = calculate(first_number, second_number, operation)

    # result is None when the operation symbol was invalid
    if result is not None:
        print(f"Result: {first_number} {operation} {second_number} = {result}")

except ValueError:
    # Runs when input could not be converted to a number
    print("Error: please enter valid numbers (for example 4 or 2.5).")

except ZeroDivisionError:
    # Runs when the user tries to divide by zero
    print("Error: you cannot divide by zero.")