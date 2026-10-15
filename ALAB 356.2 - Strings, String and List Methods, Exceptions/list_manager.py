# Task 2: List Management with Error Handling

numbers = []

while True:
    # Show the menu
    print("\nMenu:")
    print("(a) Add a number")
    print("(b) Remove a number")
    print("(c) Display the list")
    print("(d) Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice == "a":
        try:
            value = int(input("Enter an integer to add: "))
            numbers.append(value)
            print(f"Added {value}.")
        except ValueError:
            print("Error: please enter a whole number (an integer).")

    elif choice == "b":
        try:
            index = int(input("Enter the index to remove: "))
            removed = numbers.pop(index)
            print(f"Removed {removed} at index {index}.")
        except ValueError:
            print("Error: the index must be a whole number (an integer).")
        except IndexError:
            print("Error: that index does not exist in the list.")

    elif choice == "c":
        print("Current list:", numbers)

    elif choice == "d":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a, b, c, or d.")