# Topics: Nested loop, 2D list, function
# Date : 7 Jan

"""
Task 1: The "Grade Scanner" (2D Lists & Functions)
The Challenge: You have a 2D list where each inner list represents a student's scores in different subjects. Write a function check_failing(grades_grid) that prints "Student [Index] failed a subject!" if any of their scores are below 50.

all_grades = [
[88, 92, 70], # Student 0 
 [45, 80, 77], # Student 1 (Has a 45!) 
 [99, 100, 95] # Student 2
]
"""
all_grades = [
    [88, 92, 70],  
    [45, 80, 77], 
    [99, 100, 95] 
]
def check_failing(all_grades):
    
    for index, num in enumerate(all_grades):
        for score in num:
            if score<50:
                print(f"Student {index} fail a Subject!")
                break
    
check_failing(all_grades)

"""
Task 2: The "Pixel Flasher" (Modifying 2D Lists)
The Challenge: In computer graphics, a screen is a 2D grid of 0s (off) and 1s (on). Write a function called activate_row(screen, row_index) that takes the grid and a row number, then uses a single loop to change every pixel in that specific row to 1.

monitor = [
[0, 0, 0], 
 [0, 0, 0], 
[0, 0, 0]
]
"""
monitor = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]

def activate_row(screen,row_index):
    selected_row=screen[row_index]
    
    for i in range(len(selected_row)):
        screen[row_index][i]=1
    

print("\n Before")
for row in monitor:
    print(row)
activate_row(monitor,2)

print("\n After")
for row in monitor:
    print(row)