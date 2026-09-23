# --- For loop version ---
total_for = 0
for num in range(1, 51):  # 1 to 50 inclusive
    if num % 2 == 0:      # check if number is even
        total_for += num
print(f"The sum of even numbers from 1 to 50 is {total_for}.")

# --- While loop version ---
total_while = 0
n = 1
while n <= 50:
    if n % 2 == 0:
        total_while += n
    n += 1
print(f"The sum of even numbers from 1 to 50 is {total_while}.")

# Both loops produce the same result (2550).
# The for loop is clearer here since we know the exact range in advance;
# the while loop needs manual counter management (n += 1).