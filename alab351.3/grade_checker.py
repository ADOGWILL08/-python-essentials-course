# Ask the user for a numeric grade
grade = float(input("Enter your numeric grade (0-100): "))

# Convert the numeric grade to a letter grade using if/elif/else
# Order matters here: we check from highest to lowest so each
# number lands in the correct bracket (handles edge cases like 100 or 0)
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Your grade is: {letter}")

# Conditional message based on passing vs. not passing
if letter in ("A", "B", "C"):
    print("Great job! Keep it up.")
else:
    print("Don't give up — review the material and try again.")