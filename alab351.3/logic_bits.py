# Logical operators
a = input("Enter True/False for A: ").strip().lower() == "true"
b = input("Enter True/False for B: ").strip().lower() == "true"

print(f"A and B: {a and b}")
print(f"A or B: {a or b}")
print(f"not A: {not a}")

# Bitwise operators on two small integers
x, y = 5, 3
print(f"x & y = {bin(x & y)}")
print(f"x | y = {bin(x | y)}")
print(f"x ^ y = {bin(x ^ y)}")
print(f"~x     = {bin(~x)}")
print(f"x << 1 = {bin(x << 1)}")
print(f"x >> 1 = {bin(x >> 1)}")