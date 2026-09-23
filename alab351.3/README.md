# ALAB 351.3 — Conditionals, Loops, and Lists

This folder contains the five Python scripts for Lab 3, along with sample terminal output for each.

## Files

- `grade_checker.py`
- `even_sum.py`
- `list_operations.py`
- `bubble_sort_demo.py`
- `logic_bits.py` (bonus)

---

## grade_checker.py

```
Enter your numeric grade (0-100): 95
Your grade is: A
Great job! Keep it up.
```

Boundary values were also tested to confirm the letter-grade cutoffs work correctly:

| Input | Output |
|---|---|
| 90 | A |
| 89 | B |
| 60 | D |
| 59 | F |

---

## even_sum.py

```
The sum of even numbers from 1 to 50 is 650.
The sum of even numbers from 1 to 50 is 650.
```

Both the `for` loop version and the `while` loop version produce the same result (650), confirming the two approaches are equivalent. The `for` loop is arguably clearer here since the range (1 to 50) is known in advance, while the `while` loop requires manually incrementing and checking a counter.

---

## list_operations.py

```
Original list: [8, 3, 15, 1, 9]
Sorted (new list): [1, 3, 8, 9, 15]
Original still unchanged: [8, 3, 15, 1, 9]
Sorted in place: [1, 3, 8, 9, 15]
After append: [1, 3, 8, 9, 15, 20]
After removing 1: [3, 8, 9, 15, 20]
Reversed list: [20, 15, 9, 8, 3]
```

---

## bubble_sort_demo.py

```
After pass 1: [25, 12, 22, 11, 64]
After pass 2: [12, 22, 11, 25, 64]
After pass 3: [12, 11, 22, 25, 64]
After pass 4: [11, 12, 22, 25, 64]
After pass 5: [11, 12, 22, 25, 64]
Final sorted list: [11, 12, 22, 25, 64]
```

---

## logic_bits.py (bonus)

```
Enter True/False for A: True
Enter True/False for B: False
A and B: False
A or B: True
not A: False
x & y = 0b1
x | y = 0b111
x ^ y = 0b110
~x     = -0b110
x << 1 = 0b1010
x >> 1 = 0b10
```
