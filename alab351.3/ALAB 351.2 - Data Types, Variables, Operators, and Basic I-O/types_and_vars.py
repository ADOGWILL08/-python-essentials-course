# types_and_vars.py
# Purpose: Practice variables, data types, operators, and printing output.

# --- Variables and introduction ---
name = "Alice"    # str (string): text
age = 20          # int (integer): whole number
height = 1.65     # float: decimal number, in meters

# An f-string (the f before the quotes) lets us put variables inside {}
print(f"Hello, my name is {name}. I am {age} years old and {height} meters tall.")

# --- Age in 5 years (addition operator) ---
age_in_5_years = age + 5
print(f"In 5 years, I will be {age_in_5_years} years old.")

# --- Rectangle area (multiplication operator) ---
width = 5.5
rect_height = 2   # named rect_height so it doesn't overwrite our height variable above
area = width * rect_height
print(f"The area of a {width} x {rect_height} rectangle is {area}.")

# --- More arithmetic operators ---
years_until_30 = 30 - age       # subtraction
half_age = age / 2              # true division (always gives a float)
print(f"Years until I turn 30: {years_until_30}")
print(f"Half of my age: {half_age}")

# --- String operations ---
greeting = "Hello, " + name     # concatenation: joining strings with +
print(greeting)
print("-" * 20)                 # repetition: repeats the string 20 times