def get_grade_point(ct, mid, final):
    """
    Calculates Grade Point based on total marks.
    Scale: 80-100: 4.00, 75-79: 3.75, 70-74: 3.50, etc.
    """
    total_marks = ct + mid + final
    
    if total_marks >= 80:
        return 4.00
    elif total_marks >= 75:
        return 3.75
    elif total_marks >= 70:
        return 3.50
    elif total_marks >= 65:
        return 3.25
    elif total_marks >= 60:
        return 3.00
    elif total_marks >= 55:
        return 2.75
    elif total_marks >= 50:
        return 2.50
    elif total_marks >= 45:
        return 2.25
    elif total_marks >= 40:
        return 2.00
    else:
        return 0.00

def run_fixed_credit_system():
    print("--- Fixed Credit Grading System ---")
    print("Available Departments: CSE, EEE, Civil, BBA, English")
    dept = input("Enter Department Name: ")

    # Variables to accumulate weighted points and total credits
    # These must be reset inside each block or initialized here
    total_weighted_points = 0.0
    total_credits = 0.0

    if dept == "CSE":
        print("\n--- Department: CSE (Fixed Credits) ---")
        
        # Subject 1: Programming (3 Credits)
        print("Subject: Intro to Programming (3.0 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 3.0)
        total_credits = total_credits + 3.0

        # Subject 2: Discrete Math (3 Credits)
        print("\nSubject: Discrete Math (3.0 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 3.0)
        total_credits = total_credits + 3.0

        # Subject 3: Lab (1.5 Credits)
        print("\nSubject: Programming Lab (1.5 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 1.5)
        total_credits = total_credits + 1.5

    elif dept == "EEE":
        print("\n--- Department: EEE (Fixed Credits) ---")
        
        # Subject 1: Circuits I (3 Credits)
        print("Subject: Circuits I (3.0 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 3.0)
        total_credits = total_credits + 3.0
        
        # Subject 2: Electronics (3 Credits)
        print("\nSubject: Basic Electronics (3.0 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 3.0)
        total_credits = total_credits + 3.0

    elif dept == "Civil":
        print("\n--- Department: Civil (Fixed Credits) ---")
        
        # Subject 1: Mechanics (4 Credits)
        print("Subject: Engineering Mechanics (4.0 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 4.0)
        total_credits = total_credits + 4.0

        # Subject 2: Drawing (2 Credits)
        print("\nSubject: Engineering Drawing (2.0 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 2.0)
        total_credits = total_credits + 2.0

    elif dept == "BBA":
        print("\n--- Department: BBA (Fixed Credits) ---")
        
        # Subject 1: Accounting (3 Credits)
        print("Subject: Intro to Accounting (3.0 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 3.0)
        total_credits = total_credits + 3.0

        # Subject 2: Management (3 Credits)
        print("\nSubject: Principles of Management (3.0 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 3.0)
        total_credits = total_credits + 3.0

    elif dept == "English":
        print("\n--- Department: English (Fixed Credits) ---")
        
        # Subject 1: Literature (3 Credits)
        print("Subject: Intro to Literature (3.0 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 3.0)
        total_credits = total_credits + 3.0

        # Subject 2: Phonetics (3 Credits)
        print("\nSubject: Phonetics (3.0 Credits)")
        ct = float(input("Enter Class Test (0-30): "))
        mid = float(input("Enter Mid Term (0-30): "))
        final = float(input("Enter Final Term (0-40): "))
        gp = get_grade_point(ct, mid, final)
        total_weighted_points = total_weighted_points + (gp * 3.0)
        total_credits = total_credits + 3.0

    else:
        print("Invalid Department Name")
        return

    # Final Calculation
    if total_credits > 0:
        cgpa = total_weighted_points / total_credits
        print("\n------------------------------")
        print(f"Calculated CGPA for {dept}: {cgpa:.2f}")
    else:
        print("No credits calculated.")

# Execute
run_fixed_credit_system()