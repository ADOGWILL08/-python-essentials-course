import datetime
import os

# Name of the diary file (kept in the current directory)
DIARY_FILE = "diary.txt"


def ensure_diary_exists(filename):
    """Create the diary file if it does not exist yet."""
    if not os.path.exists(filename):
        print(f"{filename} not found. Creating a new diary file...")
        # Mode "w" creates an empty file
        with open(filename, "w", encoding="utf-8"):
            pass
    else:
        print(f"{filename} found. New entries will be added to it.")


def add_entry(filename, entry):
    """Append a timestamped entry to the diary file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Mode "a" appends to the end without erasing old entries
    with open(filename, "a", encoding="utf-8") as diary:
        diary.write(f"[{timestamp}] {entry}\n")


def show_diary(filename):
    """Read and print the whole diary file."""
    with open(filename, "r", encoding="utf-8") as diary:
        content = diary.read()
    print("\n--- Your Diary ---")
    print(content, end="")
    print("--- End of Diary ---")


def main():
    """Run the diary program."""
    try:
        ensure_diary_exists(DIARY_FILE)

        entry = input("Write your diary entry: ").strip()
        if entry:
            add_entry(DIARY_FILE, entry)
            print("Entry saved.")
        else:
            print("No entry was typed, so nothing was added.")

        show_diary(DIARY_FILE)

    except PermissionError:
        print(f"Error: no permission to use {DIARY_FILE}.")
    except OSError as error:
        print(f"File error: {error}")
    except EOFError:
        print("Error: no input was received.")


if __name__ == "__main__":
    main()