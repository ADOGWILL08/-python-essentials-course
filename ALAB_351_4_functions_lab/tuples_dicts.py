# tuples_dicts.py
# Lab 4 - Part 2: Working with tuples and dictionaries


# ---------------- Tuples ----------------

# A tuple of the twelve months. Tuples use parentheses and cannot be changed
# after they are created (they are "immutable").
months = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

# Index 0 is the first item. Index -1 counts back from the end, so it's the last item.
print(f"First month: {months[0]}")
print(f"Last month: {months[-1]}")

# Try to change the first item in the tuple. This should fail, because
# tuples do not allow their items to be changed after creation.
try:
    months[0] = "NewMonth"
except TypeError as e:
    # "as e" stores the error's message so we can print it
    print(f"Tuples are immutable, error: {e}")


# ---------------- Dictionaries ----------------

# A dictionary of students and their grades. Names are the keys, grades are the values.
students = {
    "Alice": 90,
    "Ben": 78,
    "Chloe": 85,
    "David": 92
}

# Add a new student and grade
students["Emma"] = 88

print("\nAll students after adding Emma:")
print(students)

# Update an existing student's grade
students["Ben"] = 81

print(f"\nUpdated entry for Ben: {students['Ben']}")

# Loop through the dictionary and print each name and grade in a clear format
print("\nAll students, formatted:")
for name, grade in students.items():
    print(f"{name}: {grade}")