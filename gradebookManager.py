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
    choice = input("Would you like to add a new student, add grades for an existing student, remove a student or grade, or view the gradebook summary (enter new student, add grade, remove, or view): ").strip().lower()
    if choice == "new student":
        print()
        print(gradebook)
        print()
        add_students = input("What is the name of the student you would like to add: ").strip().capitalize()
        print()
        new_student_grades = input("What grade would you like to input for this student (Enter just the number): ").strip()
        gradebook[add_students] = new_student_grades
        print()
        print(add_students + " has been added into the gradebook.")
        print()
        print(gradebook)
        print()

    if choice == "add grade":
        print()
        print(gradebook)
        print()
        name = input("What is the name of the existing student that you want to add a grade for?: ").strip().capitalize()
        print()
        new_grade = input("What is the grade you want to add (Enter only the number): ")
        gradebook[name].append(new_grade)
        print()
        print("The grade " + new_grade + " has been added to " + name + "'s grades.")
        print()
        print(gradebook)
        print()

    if choice == "remove":
        print()
        print(gradebook)
        print()
        what = input("Would you like to remove a student or a student's grade (enter grade or student): ").strip().lower()
        print()
        if what == "grade":
            student_name = input("What is the name of the student whose grade you wish to remove?: ").strip().capitalize()
            print()
            remove_grade = input("What is the grade you wish to remove (enter only the number)?: ")
            gradebook[student_name].remove(int(remove_grade))
            print()
            print("The grade " + remove_grade + " has been removed from " + student_name + "'s grades.")
            print()
            print(gradebook)
            print()
        if what == "student":
            student_name = input("What is the name of the student that you wish to remove?: ").strip().capitalize()
            print()
            del gradebook[student_name]
            print(student_name + " has been removed from the gradebook.")
            print()
            print(gradebook)
            print()    

    if choice == "view":
        print()
        break


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