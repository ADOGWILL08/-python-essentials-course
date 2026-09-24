# simple_calculator.py
# Purpose: Ask the user for two numbers and an operation, then print the result.

print("=== Simple Calculator ===")

# input() always returns a string, so we convert each entry to a float.
# try/except catches the error if the user types something that isn't a number.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: please enter numbers only (for example 7 or 3.5).")
else:
    # This part only runs if both numbers were converted successfully.
    operation = input("Choose an operation (+, -, *, /): ")

    # if/elif/else picks the right calculation based on the symbol entered.
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        # Dividing by zero causes a crash, so we check for it first.
        if num2 == 0:
            print("Error: you cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        # Runs if the symbol didn't match any of the four operations above.
        print("Error: unsupported operation. Please use +, -, * or /.")