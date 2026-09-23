numbers = [64, 25, 12, 22, 11]
n = len(numbers)

# Outer loop: controls number of passes through the list
for i in range(n):
    # Inner loop: compares each pair of adjacent elements
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap if left element is bigger than right
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print(f"After pass {i + 1}: {numbers}")

print("Final sorted list:", numbers)