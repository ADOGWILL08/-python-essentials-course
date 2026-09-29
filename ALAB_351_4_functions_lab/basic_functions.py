# basic_functions.py
# Lab 4 - Part 1: Writing and using simple functions


def greet_user(name=""):
    """
    Prints a greeting for the user.

    Parameter:
        name (str): the person's name. It defaults to an empty string,
                    so the function still works when no name is given.
    Returns:
        Nothing (it only prints the greeting).
    """
    # An empty string counts as False in an if statement,
    # so this branch only runs when a real name was provided.
    if name:
        print(f"Hello, {name}! Welcome!")
    else:
        print("Hello! Welcome!")


def add_two_numbers(a, b):
    """
    Adds two numbers together.

    Parameters:
        a (int or float): the first number
        b (int or float): the second number
    Returns:
        The sum of a and b.
    """
    return a + b


def is_even(num):
    """
    Checks whether a number is even.

    Parameter:
        num (int): the number to check
    Returns:
        True if num is even, otherwise False.
    """
    # % gives the remainder after division. Even numbers leave a remainder of 0.
    return num % 2 == 0


# ---------------- Main part of the script ----------------

# Demonstrate greet_user with a name and without a name
greet_user("Alex")
greet_user()

# Demonstrate add_two_numbers and store the returned value in a variable
total = add_two_numbers(5, 7)
print(f"5 + 7 = {total}")

# Demonstrate is_even with one even number and one odd number
print(f"4 is even: {is_even(4)}")
print(f"7 is even: {is_even(7)}")

# Show that returned values can be used in expressions:
# the sum from add_two_numbers is passed straight into is_even
if is_even(total):
    print(f"The sum {total} is an even number.")
else:
    print(f"The sum {total} is an odd number.")

# One function call used inside another
bigger_total = add_two_numbers(total, add_two_numbers(1, 2))
print(f"{total} + (1 + 2) = {bigger_total}")