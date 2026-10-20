"""task.py - Defines the Task class for the To-Do List Manager."""

from datetime import date


class Task:
    """Represents a single to-do item."""

    def __init__(self, title, due_date=None, completed=False):
        """Set up a new task.

        title: short description of the task (string)
        due_date: optional due date (datetime.date object or string)
        completed: True if the task is done, False otherwise
        """
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        """Return a readable string, e.g. '[-] Submit assignment (due 2025-03-10)'."""
        status = "X" if self.completed else "-"
        if self.due_date:
            return f"[{status}] {self.title} (due {self.due_date})"
        return f"[{status}] {self.title}"


# This block only runs when you run task.py directly (not when other files import it).
if __name__ == "__main__":
    task1 = Task("Submit assignment", "2025-03-10")
    task2 = Task("Read chapter 5", date(2026, 10, 25), completed=True)
    task3 = Task("Buy groceries")
    print(task1)
    print(task2)
    print(task3)