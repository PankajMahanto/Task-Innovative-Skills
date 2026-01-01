import math

def print_header():
    print("\n" + "="*40)
    print("      SCIENTIFIC CALCULATOR (CLI)      ")
    print("="*40)

def show_options():
    print("""
1. Basic: +, -, *, /, %, ** (Power)
2. Roots: sqrt (√), cbrt (∛), absolute (|x|)
3. Trig:  sin, cos, tan, asin, acos, atan
4. Log:   log10, ln (natural log), e^x, 10^x
5. Round: round, floor, ceil, gcd, lcm
6. Const: PI (π), Euler's Number (e)
7. Misc:  Factorial (n!)
0. EXIT
    """)

def calculator():
    while True:
        print_header()
        show_options()
        
        choice = input("Select a category (0-7): ")

        try:
            # EXIT
            if choice == '0':
                print("Closing Calculator. Goodbye!")
                break

            # 1. BASIC ARITHMETIC
            elif choice == '1':
                expr = input("Enter basic expression (e.g. 10 + 5 * 2): ")
                # eval evaluates the string as a mathematical expression
                print(f"Result: {eval(expr)}")

            # 2. ROOTS & ABSOLUTE
            elif choice == '2':
                num = float(input("Enter number: "))
                print(f"Square Root: {math.sqrt(num)}")
                print(f"Cube Root: {num**(1/3)}")
                print(f"Absolute: {abs(num)}")

            # 3. TRIGONOMETRY
            elif choice == '3':
                op = input("Choose (sin, cos, tan, asin, acos, atan): ").lower()
                val = float(input("Enter value: "))
                
                # Check if user is using degrees or radians for standard trig
                if op in ['sin', 'cos', 'tan']:
                    unit = input("Is input in (D)egrees or (R)adians? ").upper()
                    if unit == 'D':
                        val = math.radians(val)

                if op == 'sin': print(f"Result: {math.sin(val)}")
                elif op == 'cos': print(f"Result: {math.cos(val)}")
                elif op == 'tan': print(f"Result: {math.tan(val)}")
                elif op == 'asin': print(f"Result: {math.asin(val)}")
                elif op == 'acos': print(f"Result: {math.acos(val)}")
                elif op == 'atan': print(f"Result: {math.atan(val)}")

            # 4. LOG & EXPONENTIAL
            elif choice == '4':
                op = input("Choose (log, ln, exp, 10x): ").lower()
                num = float(input("Enter value: "))
                if op == 'log': print(f"Result: {math.log10(num)}")
                elif op == 'ln': print(f"Result: {math.log(num)}")
                elif op == 'exp': print(f"Result: {math.exp(num)}")
                elif op == '10x': print(f"Result: {10**num}")

            # 5. ROUNDING & NUMBER OPS
            elif choice == '5':
                num = float(input("Enter number: "))
                print(f"Round: {round(num)}")
                print(f"Floor: {math.floor(num)}")
                print(f"Ceil: {math.ceil(num)}")
                
                # GCD/LCM require integers
                if num.is_integer():
                    num2 = int(input("Enter second integer for GCD/LCM: "))
                    print(f"GCD: {math.gcd(int(num), num2)}")
                    print(f"LCM: {math.lcm(int(num), num2)}")

            # 6. CONSTANTS
            elif choice == '6':
                print(f"Value of PI (π): {math.pi}")
                print(f"Value of Euler's Number (e): {math.e}")

            # 7. FACTORIAL
            elif choice == '7':
                num = int(input("Enter a positive integer: "))
                print(f"{num}! = {math.factorial(num)}")

            else:
                print("Invalid choice! Please select 0-7.")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Error: Invalid input (math domain error or non-numeric).")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    calculator()