# ALAB 351.4 - Functions, Tuples, Dictionaries, and Exceptions

## Part 1: Functions

### basic_functions.py
Defines `greet_user()` (with a default parameter to handle a missing name), `add_two_numbers(a, b)`, and `is_even(num)`.

**Sample output:**
```
Hello, Alex! Welcome!
Hello! Welcome!
5 + 7 = 12
4 is even: True
7 is even: False
The sum 12 is an even number.
12 + (1 + 2) = 15
```

**What I learned:** a default parameter (`name=""`) lets a function run correctly whether or not an argument is passed in. `return` lets a function's result be stored in a variable and reused, including passing one function's return value into another function.

### calc_with_functions.py
Refactors the calculator into `add`, `subtract`, `multiply`, `divide`, and a `calculate(a, b, op)` function that picks the right one.

**Sample output (4 test runs):**
```
Enter the first number: 10
Enter the second number: 4
Enter an operation (+, -, *, /): +
Result: 10.0 + 4.0 = 14.0

Enter the first number: 8
Enter the second number: 0
Enter an operation (+, -, *, /): /
Error: you cannot divide by zero.

Enter the first number: abc
Error: please enter valid numbers (for example 4 or 2.5).

Enter the first number: 6
Enter the second number: 3
Enter an operation (+, -, *, /): %
Error: '%' is not a valid operation. Use +, -, * or /.
```

**How exceptions were caught and handled:** a `try/except` block wraps the user input and the `calculate()` call. `except ValueError` catches text that can't be converted to a number with `float()`. `except ZeroDivisionError` catches an attempt to divide by zero. An invalid operation symbol (like `%`) isn't an exception at all — `calculate()` checks for it with `if/elif/else` and prints its own error message.

## Part 2: Tuples and Dictionaries

### tuples_dicts.py
Creates a `months` tuple, prints its first/last items, tries to modify it, and works with a `students` dictionary.

**Sample output:**
```
First month: January
Last month: December
Tuples are immutable, error: 'tuple' object does not support item assignment

All students after adding Emma:
{'Alice': 90, 'Ben': 78, 'Chloe': 85, 'David': 92, 'Emma': 88}

Updated entry for Ben: 81

All students, formatted:
Alice: 90
Ben: 81
Chloe: 85
David: 92
Emma: 88
```

**How exceptions were caught and handled:** trying to assign `months[0] = "NewMonth"` raises a `TypeError`, because tuples don't support item assignment. `except TypeError as e:` catches it and prints the error's own message, proving tuples are immutable.

### data_processing.py
Defines `get_average_grade(grades_tuple)` and loops over a `course_grades` dictionary, including one course (History) with an empty tuple.

**Sample output:**
```
Course averages:
The average grade for Math is 86.2
The average grade for Science is 84.3
Warning: no grades available to calculate an average.
The average grade for History could not be calculated (no grades).
```

**How exceptions were caught and handled:** `get_average_grade` divides by `len(grades_tuple)`, which is `0` for an empty tuple. `except ZeroDivisionError` catches that, prints a warning, and returns `None` instead of crashing. The main loop checks `if average is None:` to print a clear message for that edge case.

## Part 3: Exception Handling

### exception_demo.py
Defines `safe_divide(a, b)`, which raises its own `ValueError` when dividing by zero, and demonstrates catching a generic `Exception`.

**Sample output:**
```
10 / 2 = 5.0
Division operation completed
Error: Cannot divide by zero
Division operation completed

Now demonstrating a generic exception:
An unexpected error occurred: invalid literal for int() with base 10: 'not_a_number'
Conversion attempt completed
```

**How exceptions were caught and handled:** `safe_divide` deliberately raises `ValueError("Cannot divide by zero")` when `b` is zero, instead of waiting for Python to raise its own error. A `try/except ValueError` around the calls catches it and prints a friendly message, and a `finally` clause always prints `"Division operation completed"`, whether or not an error occurred. Separately, `int("not_a_number")` raises an error on its own, and `except Exception as e:` catches it generically as a safety net, followed by its own `finally` clause.