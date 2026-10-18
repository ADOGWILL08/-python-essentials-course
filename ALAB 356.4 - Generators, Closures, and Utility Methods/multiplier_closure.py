def make_multiplier(factor):
    """Return a function that multiplies any number by factor."""
    # Make sure the factor is a number before we remember it
    if not isinstance(factor, (int, float)):
        raise TypeError("factor must be a number")

    def multiplier(x):
        """Multiply x by the factor remembered from the outer function."""
        return x * factor

    # Return the inner function itself (no parentheses), not its result
    return multiplier


# --- Test code ---
# This block only runs when you run this file directly
if __name__ == "__main__":
    times3 = make_multiplier(3)
    times10 = make_multiplier(10)

    print("Closure demonstration:")
    print(f"times3(7) = {times3(7)}")
    print(f"times10(7) = {times10(7)}")
    print(f"times3(10) = {times3(10)}")
    print(f"times10(2.5) = {times10(2.5)}")

    # Show that bad input is handled gracefully
    try:
        make_multiplier("abc")
    except TypeError as error:
        print(f"Error: {error}")