# string_fun.py
# Purpose: Practice string operations on a word the user types in.

# Ask the user for a word (input() returns a string).
word = input("Enter a word: ")

# len() counts the number of characters in the string.
print(f"Length: {len(word)}")

# .upper() returns the word in all capital letters.
print(f"Uppercase: {word.upper()}")

# The * operator repeats a string, so word * 3 gives the word three times in a row.
print(f"Repeated 3 times: {word * 3}")