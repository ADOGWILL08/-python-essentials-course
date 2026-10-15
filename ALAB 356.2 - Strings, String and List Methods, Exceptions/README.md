# ALAB 356.2 - Strings, String and List Methods, Exceptions

This lab contains three Python scripts. Sample outputs from my test runs are shown below each script.

## Task 1: string_manipulation.py

Prompts for a sentence, then prints it in uppercase, reversed, with a vowel count, and with spaces replaced by hyphens.

```
Enter a sentence: Hello World
Uppercase: HELLO WORLD
Reversed: dlroW olleH
Number of vowels: 3
Hyphenated: Hello-World
```

## Task 2: list_manager.py

A menu-driven program to add, remove, and display integers, with error handling for non-integer input and invalid indexes. (The menu that prints before each choice is left out of this log to keep it short.)

```
Choose an option: a
Enter an integer to add: 5
Added 5.
Choose an option: c
Current list: [5]
Choose an option: a
Enter an integer to add: 10
Added 10.
Choose an option: a
Enter an integer to add: abc
Error: please enter a whole number (an integer).
Choose an option: c
Current list: [5, 10]
Choose an option: b
Enter the index to remove: xyz
Error: the index must be a whole number (an integer).
Choose an option: b
Enter the index to remove: 99
Error: that index does not exist in the list.
Choose an option: b
Enter the index to remove: 0
Removed 5 at index 0.
Choose an option: z
Invalid choice. Please enter a, b, c, or d.
Choose an option: d
Goodbye!
```

## Task 3: age_validator.py

Uses a `validate_age` function that raises a `ValueError` for ages outside 0-120. The script catches the error and prints the message. Each run below is a separate run of the script.

```
Enter your age: 25
Age 25 is accepted.

Enter your age: 0
Age 0 is accepted.

Enter your age: 120
Age 120 is accepted.

Enter your age: -5
Error: Invalid age: -5. Age must be between 0 and 120.

Enter your age: 121
Error: Invalid age: 121. Age must be between 0 and 120.

Enter your age: 150
Error: Invalid age: 150. Age must be between 0 and 120.

Enter your age: abc
Error: invalid literal for int() with base 10: 'abc'
```