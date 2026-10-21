# Personal To-Do List Manager

A console application for managing daily tasks, built for SBA 356 Python Essentials 2.

## Features

- Add tasks with an optional due date (YYYY-MM-DD)
- Mark tasks as completed
- Delete tasks
- List tasks with numbers, status, and due dates
- Overdue tasks are flagged (red when `colorama` is installed)
- Tasks are saved to `tasks.json` and loaded again on startup
- Friendly error messages for bad dates, bad task numbers, and file problems

## Files

| File | Purpose |
|---|---|
| `task.py` | The `Task` class |
| `todolist.py` | Functions to add, complete, delete, list, save, and load tasks |
| `main.py` | The text menu (run this file) |
| `tasks.json` | Saved task data |
| `requirements.txt` | Optional package (`colorama`) |
| `sample_output.txt` | Text log of demo runs |

## How to run

1. (Optional, for colored output) install the package:

```
   pip install colorama
```

2. Run the program from this folder:

```
   python main.py
```

3. Choose an option: (A) Add, (C) Complete, (D) Delete, (L) List, (Q) Quit.
   When you quit, the program asks whether to save your tasks.

## Sample output

`sample_output.txt` shows runs that add, list, complete, and delete tasks,
save them, and then load the saved tasks on the next start. It also shows
the friendly error message for an invalid task number.