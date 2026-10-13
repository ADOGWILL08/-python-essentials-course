# builtin_usage.py
# Task 1: Using built-in modules (math, random, platform)

# Import the built-in modules we need
import math
import random
import platform

# Generate a random integer between 1 and 100 (both ends included)
random_number = random.randint(1, 100)

# Calculate the square root, then round DOWN to a whole number
square_root_floored = math.floor(math.sqrt(random_number))

# Get system information from the platform module
os_name = platform.system()              # e.g. "Windows", "Darwin" (Mac), "Linux"
python_version = platform.python_version()  # e.g. "3.12.4"

# Print each result with a descriptive label
print("Random Number:", random_number)
print("Square Root (floored):", square_root_floored)
print("Operating System:", os_name)
print("Python Version:", python_version)