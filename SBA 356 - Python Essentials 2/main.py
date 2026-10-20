"""main.py - Text-based menu for the To-Do List Manager."""

from todolist import add_task, complete_task, delete_task, list_tasks, save_tasks

MENU = """
===== To-Do List Manager =====
(A) Add a new task
(C) Mark a task as completed
(D) Delete a task
(L) List all tasks
(Q) Quit
==============================
"""


def ask_for_index(task_list, prompt):
    """Ask the user for a task number (1, 2, 3...) and return a 0-based index.

    Returns None if the input is not a valid task number.
    """
    text = input(prompt).strip()
    try:
        number = int(text)
    except ValueError:
        print("Error: please enter a whole number, like 2.")
        return None

    if number < 1 or number > len(task_list):
        print(f"Error: there is no task number {number}.")
        return None

    return number - 1  # Python lists start counting at 0


def ask_to_save(task_list):
    """Ask whether to save before quitting, and save if the user says yes."""
    while True:
        answer = input("Save your tasks to a file before quitting? (Y/N): ")
        answer = answer.strip().upper()
        if answer == "Y":
            if save_tasks(task_list):
                print("Tasks saved to tasks.json.")
            return
        if answer == "N":
            print("Tasks were not saved.")
            return
        print("Please type Y or N.")


def main():
    """Run the menu loop until the user chooses to quit."""
    tasks = []

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip().upper()

        if choice == "A":
            title = input("Task title: ")
            due = input("Due date (YYYY-MM-DD, or press Enter for none): ")
            new_task = add_task(tasks, title, due)
            if new_task:
                print(f"Added: {new_task}")

        elif choice == "C":
            if not tasks:
                print("Your to-do list is empty.")
                continue
            list_tasks(tasks)
            index = ask_for_index(tasks, "Enter the number of the task to complete: ")
            if index is not None and complete_task(tasks, index):
                print("Task marked as completed.")

        elif choice == "D":
            if not tasks:
                print("Your to-do list is empty.")
                continue
            list_tasks(tasks)
            index = ask_for_index(tasks, "Enter the number of the task to delete: ")
            if index is not None:
                removed = delete_task(tasks, index)
                if removed:
                    print(f"Deleted: {removed}")

        elif choice == "L":
            list_tasks(tasks)

        elif choice == "Q":
            ask_to_save(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please type A, C, D, L, or Q.")


if __name__ == "__main__":
    main()