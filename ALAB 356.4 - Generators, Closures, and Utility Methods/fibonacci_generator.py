def gen_fibonacci(n):
    """Generator that yields the first n Fibonacci numbers.

    The sequence starts 0, 1, 1, 2, 3, 5, 8, ...
    """
    # Make sure n is a whole number that is not negative
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative whole number")

    # 'a' is the current number, 'b' is the next number
    a, b = 0, 1
    for _ in range(n):
        yield a          # hand back the current number, then pause here
        a, b = b, a + b  # slide forward: next becomes current, add for new next


# --- Test code ---
# This block only runs when you run this file directly
if __name__ == "__main__":
    count = 10
    print(f"The first {count} Fibonacci numbers:")

    try:
        for position, number in enumerate(gen_fibonacci(count), start=1):
            print(f"Fibonacci number {position}: {number}")
    except ValueError as error:
        print(f"Error: {error}")