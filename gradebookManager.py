#Requirements
#1. Create a Gradebook
#- Use a dictionary where keys are student names and values are lists of grades.
#- Add at least 3 students initially, each with at least 3 grades.
gradebook = {
    "Alice": [90, 85, 92],
    "Bob": [78, 81, 86],
    "Chloe": [64, 75, 70]
}

#2. User Input
#- Allow the user to:
#  - Add a new student
#  - Add grades for an existing student
#  - View the gradebook summary
while True:
    choice = input("Would you like to add a new student, add grades for an existing student, or view the gradebook summary (enter new student, add grade, or view): ")
#3. Calculations
#- For each student, calculate the average grade.
#- Identify and print the student with the highest average.

#4. Display
#- Print a clear summary of all students, their grades, and their average.
#- Example output:
#  - Alice: [90, 85, 92] Average: 89.0
#  - Bob: [78, 81, 86] Average: 81.7
#  - Top Student: Alice

#5. Additional Features (Required)
#- Allow the user to remove a student or a grade.
#- Display letter grades (A, B, C, etc.) based on averages.
#- Sort students by average grade.