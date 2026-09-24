# ALAB 351.2 - Data Types, Variables, Operators, and Basic I/O

This folder contains the Python scripts for Lab 2, along with example output from running each one.

## Files

- `types_and_vars.py`
- `simple_calculator.py`
- `string_fun.py` (bonus)

## types_and_vars.py

Example output:

```
Hello, my name is Alice. I am 20 years old and 1.65 meters tall.
In 5 years, I will be 25 years old.
The area of a 5.5 x 2 rectangle is 11.0.
Years until I turn 30: 10
Half of my age: 10.0
Hello, Alice
--------------------
```

## simple_calculator.py

Multiplication (7 * 3):

```
=== Simple Calculator ===
Enter the first number: 7
Enter the second number: 3
Choose an operation (+, -, *, /): *
7.0 * 3.0 = 21.0
```

Addition (10 + 4):

```
=== Simple Calculator ===
Enter the first number: 10
Enter the second number: 4
Choose an operation (+, -, *, /): +
10.0 + 4.0 = 14.0
```

Subtraction (10 - 4):

```
=== Simple Calculator ===
Enter the first number: 10
Enter the second number: 4
Choose an operation (+, -, *, /): -
10.0 - 4.0 = 6.0
```

Division (10 / 4):

```
=== Simple Calculator ===
Enter the first number: 10
Enter the second number: 4
Choose an operation (+, -, *, /): /
10.0 / 4.0 = 2.5
```

Division by zero (10 / 0):

```
=== Simple Calculator ===
Enter the first number: 10
Enter the second number: 0
Choose an operation (+, -, *, /): /
Error: you cannot divide by zero.
```

Non-numeric input (abc):

```
=== Simple Calculator ===
Enter the first number: abc
Error: please enter numbers only (for example 7 or 3.5).
```

Unsupported operation (5, 2, %):

```
=== Simple Calculator ===
Enter the first number: 5
Enter the second number: 2
Choose an operation (+, -, *, /): %
Error: unsupported operation. Please use +, -, * or /.
```

## string_fun.py

Example 1 (python):

```
Enter a word: python
Length: 6
Uppercase: PYTHON
Repeated 3 times: pythonpythonpython
```

Example 2 (Hello):

```
Enter a word: Hello
Length: 5
Uppercase: HELLO
Repeated 3 times: HelloHelloHello
```