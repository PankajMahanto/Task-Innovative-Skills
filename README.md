# Task Innovative Skills

A collection of Python learning tasks demonstrating conditional statements, list operations, and scientific computations. This repository contains small command-line scripts intended for practice and demonstration.

## Project Overview

Contains three scripts:

- `calculator.py` — A command-line scientific calculator with basic, trigonometric, logarithmic, rounding, and constant operations.
- `conditional_Statement_task.py` — Fixed-credit grade point and CGPA calculator (department-specific course lists).
- `List_task.py` — Simple list-processing exercises: cleaning, calibration, and filtering example.

## Files & Quick Usage

- **calculator.py**

  - Run: `python calculator.py`
  - Interactive menu with categories: Basic, Roots, Trig, Log/Exp, Rounding, Constants, Factorial.

- **conditional_Statement_task.py**

  - Run: `python conditional_Statement_task.py`
  - Enter a department (CSE, EEE, Civil, BBA, English) and marks for each subject to compute CGPA.

- **List_task.py**
  - Run: `python List_task.py`
  - Demonstrates: replacing error markers, applying an in-place multiplier (calibration), and filtering low-quality readings.

---

**Scientific Calculator — Highlights**

- Basic arithmetic: `+`, `-`, `*`, `/`, `%`, `**` (power)
- Roots & absolute: square root, cube root, absolute value
- Trigonometry: `sin`, `cos`, `tan`, `asin`, `acos`, `atan` (supports degrees or radians)
- Log & exp: `log10`, `ln`, `e^x`, `10^x`
- Rounding & number ops: `round`, `floor`, `ceil`, `gcd`, `lcm`
- Constants: `pi`, `e`
- Factorial

**Calculator Example**

```
Select a category (0-7): 1
Enter basic expression (e.g. 10 + 5 * 2): 25 + 10
Result: 35
```

**Notes**

- Uses Python's `math` module; no external dependencies.
- Basic expressions use `eval()` — avoid executing untrusted input.

---

**Conditional Statement Task — Highlights**

Supported departments and example course credits:

- CSE: Intro to Programming (3.0), Discrete Math (3.0), Programming Lab (1.5)
- EEE: Circuits I (3.0), Basic Electronics (3.0)
- Civil: Engineering Mechanics (4.0), Engineering Drawing (2.0)
- BBA: Intro to Accounting (3.0), Principles of Management (3.0)
- English: Intro to Literature (3.0), Phonetics (3.0)

Grading scale (total marks → grade point):

| Total Marks | Grade Point |
| ----------- | ----------- |
| 80-100      | 4.00        |
| 75-79       | 3.75        |
| 70-74       | 3.50        |
| 65-69       | 3.25        |
| 60-64       | 3.00        |
| 55-59       | 2.75        |
| 50-54       | 2.50        |
| 45-49       | 2.25        |
| 40-44       | 2.00        |
| Below 40    | 0.00        |

Operation: for each subject enter Class Test (0-30), Mid Term (0-30), Final Term (0-40). The script computes grade points, weighted points, and final CGPA.

**Conditional Example**

```
Enter Department Name: CSE
Subject: Intro to Programming (3.0 Credits)
Enter Class Test (0-30): 25
Enter Mid Term (0-30): 28
Enter Final Term (0-40): 35
...
Calculated CGPA for CSE: 3.65
```

---

**List Task — Highlights**

`List_task.py` demonstrates basic list processing:

- Cleaning: find and replace error markers (e.g., replace "Error" with `0.0`).
- Calibration: modify values in-place (e.g., apply a 10% multiplier).
- Filtering: extract values below a quality threshold into a separate list.

Example behavior:

```
Original List: [12.5, 'Error', 18.2, 15.0, 'Error', 22.1, 10.8]
After Cleaning: [12.5, 0.0, 18.2, 15.0, 0.0, 22.1, 10.8]
After Calibration (+10%): [13.75, 0.0, 20.02, 16.5, 0.0, 24.31, 11.88]
Low Quality Log: [13.75, 0.0, 16.5, 0.0, 11.88]
```

---

## Requirements

- Python 3.6+
- No external packages required (uses built-in `math` module)

## Running the examples

Run any script from the project root with `python`.

Windows (cmd.exe) example:

```cmd
python calculator.py
python conditional_Statement_task.py
python List_task.py
```

## Contribution

Feel free to open issues or modify the scripts to add features or improve input validation. These scripts are designed for learning and can be extended.
