# Original list
numbers = [8, 3, 15, 1, 9]
print("Original list:", numbers)

# sorted() creates a new sorted list without changing the original
print("Sorted (new list):", sorted(numbers))
print("Original still unchanged:", numbers)

# .sort() sorts the list in place
numbers.sort()
print("Sorted in place:", numbers)

# Append a new element
numbers.append(20)
print("After append:", numbers)

# Remove an element by value
numbers.remove(1)
print("After removing 1:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)