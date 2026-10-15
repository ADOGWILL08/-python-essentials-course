# Task 3: Custom Exception Test (Age Validator)

def validate_age(age):
    """Raise a ValueError if age is not between 0 and 120 (inclusive)."""
    if age < 0 or age > 120:
        raise ValueError(f"Invalid age: {age}. Age must be between 0 and 120.")


user_input = input("Enter your age: ")

try:
    age = int(user_input)
    validate_age(age)
    print(f"Age {age} is accepted.")
except ValueError as error:
    print("Error:", error)