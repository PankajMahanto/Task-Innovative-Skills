# Task Innovative Skills

A collection of Python learning tasks demonstrating conditional statements and scientific computations.

## Project Overview

This project contains two main applications:

1. **Scientific Calculator (CLI)** - A comprehensive mathematical calculator
2. **Conditional Statement Task** - A student grade and CGPA calculation system

## Features

The calculator is organized into 7 main categories:

### 1. **Basic Arithmetic**

- Addition (+)
- Subtraction (-)
- Multiplication (\*)
- Division (/)
- Modulus (%)
- Power/Exponentiation (\*\*)

Example: `10 + 5 * 2`

### 2. **Roots & Absolute Value**

- Square Root (√)
- Cube Root (∛)
- Absolute Value (|x|)

### 3. **Trigonometry**

- sin, cos, tan
- asin, acos, atan
- Support for both Degrees and Radians input

### 4. **Logarithmic & Exponential**

- log10 (Base 10 Logarithm)
- ln (Natural Logarithm)
- e^x (Exponential)
- 10^x (Power of 10)

### 5. **Rounding & Number Operations**

- round
- floor
- ceil
- GCD (Greatest Common Divisor)
- LCM (Least Common Multiple)

### 6. **Mathematical Constants**

- π (PI)
- e (Euler's Number)

### 7. **Factorial**

- n! (Factorial of n)

## How to Use

1. Run the script:

   ```bash
   python calculator.py
   ```

2. The calculator will display a menu with 7 categories (0-7)

3. Select a category number to access different operations

4. Follow the prompts to enter your values

5. Enter `0` to exit the calculator

## Requirements

- Python 3.6+
- No external dependencies (uses built-in `math` module)

## Example Usage

```
Select a category (0-7): 1
Enter basic expression (e.g. 10 + 5 * 2): 25 + 10
Result: 35

Select a category (0-7): 3
Choose (sin, cos, tan, asin, acos, atan): sin
Enter value: 90
Is input in (D)egrees or (R)adians? D
Result: 1.0

Select a category (0-7): 0
Closing Calculator. Goodbye!
```

## Error Handling

- The calculator handles **Division by Zero** errors
- Invalid choice selections are detected and user is prompted to select 0-7
- Type checking for appropriate input values

## Notes

- For trigonometric functions, you can specify if input is in Degrees or Radians
- GCD and LCM operations require integer inputs
- The calculator uses Python's `eval()` function for basic arithmetic expressions, allowing flexible input formats

---

# Conditional Statement Task: Grade & CGPA Calculator

A student grading system that calculates grade points and CGPA (Cumulative Grade Point Average) based on department-specific course structures.

## Features

### Supported Departments

1. **CSE (Computer Science & Engineering)**

   - Intro to Programming (3.0 Credits)
   - Discrete Math (3.0 Credits)
   - Programming Lab (1.5 Credits)

2. **EEE (Electrical & Electronics Engineering)**

   - Circuits I (3.0 Credits)
   - Basic Electronics (3.0 Credits)

3. **Civil Engineering**

   - Engineering Mechanics (4.0 Credits)
   - Engineering Drawing (2.0 Credits)

4. **BBA (Business Administration)**

   - Intro to Accounting (3.0 Credits)
   - Principles of Management (3.0 Credits)

5. **English**
   - Intro to Literature (3.0 Credits)
   - Phonetics (3.0 Credits)

### Grading Scale

The system uses a GPA scale based on total marks:

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

## How to Use

1. Run the script:

   ```bash
   python conditional_Statement_task.py
   ```

2. Select a department from the available options (CSE, EEE, Civil, BBA, English)

3. For each subject, enter marks for:

   - Class Test (0-30)
   - Mid Term (0-30)
   - Final Term (0-40)

4. The system automatically calculates:
   - Individual subject grade points
   - Weighted grade points (GPA × Credits)
   - Final CGPA (weighted points ÷ total credits)

## Example Usage

```
--- Fixed Credit Grading System ---
Available Departments: CSE, EEE, Civil, BBA, English
Enter Department Name: CSE

--- Department: CSE (Fixed Credits) ---
Subject: Intro to Programming (3.0 Credits)
Enter Class Test (0-30): 25
Enter Mid Term (0-30): 28
Enter Final Term (0-40): 35
...
------------------------------
Calculated CGPA for CSE: 3.65
```

## How It Works

- **Conditional Logic**: Uses if-elif-else statements to determine grade points based on total marks
- **Weighted Calculation**: Multiplies each subject's grade point by its credit hours
- **CGPA Calculation**: Divides total weighted points by total credits to get final CGPA
- **Department-Specific Structure**: Each department has different course configurations and credit hours

## Requirements

- Python 3.6+
- No external dependencies
