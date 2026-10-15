# Task 1: String Manipulation Challenge

# Ask the user for a sentence and store it in a variable
sentence = input("Enter a sentence: ")

# 1. Uppercase version of the sentence
print("Uppercase:", sentence.upper())

# 2. Reversed version ([::-1] means "step backwards through the text")
print("Reversed:", sentence[::-1])

# 3. Count the vowels, ignoring upper/lower case
vowels = "aeiou"
vowel_count = 0
for char in sentence.lower():
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

# 4. Replace every space with a hyphen
print("Hyphenated:", sentence.replace(" ", "-"))