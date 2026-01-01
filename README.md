# Scientific Calculator (CLI)

A comprehensive command-line scientific calculator built with Python that supports a wide range of mathematical operations.

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
