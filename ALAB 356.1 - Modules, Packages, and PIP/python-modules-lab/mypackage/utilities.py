# utilities.py
# Custom module for Task 2: reusable helper functions

import math


def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}! Welcome to the modules lab."


def factorial(n):
    """Return the factorial of n (n must be a whole number, 0 or greater)."""
    return math.factorial(n)