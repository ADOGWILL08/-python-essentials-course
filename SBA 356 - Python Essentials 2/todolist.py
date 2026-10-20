"""todolist.py - Functions for managing a list of Task objects."""

import json
from datetime import date, datetime

from task import Task


def _get_task(task_list, index):
    """Return the task at index, or raise IndexError if the index is invalid.

    Python normally allows negative indexes (-1 is the last item), so we
    reject them here to keep indexes simple for the user.
    """
    if index < 0:
        raise IndexError("negative index")
    return task_list[index]


def is_overdue(task):
    """Return True if the task is not completed and its due date has passed."""
    return (
        not task.completed
        and isinstance(task.due_date, date)
        and task.due_date < date.today()
    )


def add_task(task_list, title, due_date=None):
    """Create a new Task and add it to task_list.

    due_date can be None, a datetime.date object, or a string in
    YYYY-MM-DD format. Returns the new Task, or None if the input was invalid.
    """
    if not title or not title.strip():
        print("Error: a task needs a title.")
        return None

    if isinstance(due_date, str):
        if due_date.strip() == "":
            due_date = None
        else:
            try:
                due_date = datetime.strptime(due_date.strip(), "%Y-%m-%d").date()
            except ValueError:
                print(
                    f"Error: '{due_date}' is not a valid date. "
                    "Use YYYY-MM-DD (for example 2026-10-25)."
                )
                return None

    new_task = Task(title.strip(), due_date)
    task_list.append(new_task)
    return new_task


def complete_task(task_list, index):
    """Mark the task at index as completed. Returns True on success."""
    try:
        task = _get_task(task_list, index)
    except (IndexError, TypeError):
        print(f"Error: there is no task with index {index}.")
        return False
    task.completed = True
    return True


def delete_task(task_list, index):
    """Remove the task at index. Returns the removed Task, or None on error."""
    try:
        _get_task(task_list, index)
    except (IndexError, TypeError):
        print(f"Error: there is no task with index {index}.")
        return None
    return task_list.pop(index)


def list_tasks(task_list):
    """Print every task with its number, status, title, and due date.

    Tasks that are past their due date and not completed are flagged OVERDUE.
    """
    if not task_list:
        print("Your to-do list is empty.")
        return

    for number, task in enumerate(task_list, start=1):
        line = f"{number}. {task}"
        if is_overdue(task):
            line += "  *** OVERDUE ***"
        print(line)


def save_tasks(task_list, filename="tasks.json"):
    """Save all tasks to a JSON file. Returns True on success, False on error."""
    data = []
    for task in task_list:
        due = task.due_date
        if isinstance(due, date):
            due = due.isoformat()  # turns a date into the text "YYYY-MM-DD"
        data.append(
            {"title": task.title, "due_date": due, "completed": task.completed}
        )

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
    except OSError as error:
        print(f"Error: could not save tasks to '{filename}' ({error}).")
        return False
    return True


# This block only runs when you run todolist.py directly (not when imported).
if __name__ == "__main__":
    tasks = []
    add_task(tasks, "Submit assignment", "2025-03-10")  # past date, so overdue
    add_task(tasks, "Read chapter 5", "2026-10-25")
    add_task(tasks, "Buy groceries")  # no due date
    add_task(tasks, "Bad date task", "10/25/2026")  # wrong format, so error
    complete_task(tasks, 1)  # marks "Read chapter 5" as done
    complete_task(tasks, 99)  # no such task, so error
    list_tasks(tasks)
    delete_task(tasks, 2)  # removes "Buy groceries"
    delete_task(tasks, -1)  # negative index, so error
    print("--- after delete ---")
    list_tasks(tasks)