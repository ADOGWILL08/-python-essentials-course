# use_utilities.py
# Task 2: Import and use the custom module from the mypackage package

# Import the utilities module from the mypackage package
from mypackage import utilities

# Call greet() and print the result with a label
greeting = utilities.greet("Adrian")
print("Greeting:", greeting)

# Call factorial() and print the result with a label
number = 5
result = utilities.factorial(number)
print("Factorial of", number, "is:", result)