#Requirements
#1. Create a Gradebook
#- Use a dictionary where keys are student names and values are lists of grades.
#- Add at least 3 students initially, each with at least 3 grades.
gradebook = {
    "Bob": [29, 91, 56],
    "Alice": [90, 85, 92],
    "Chloe": [64, 75, 70]
}

#2. User Input
#- Allow the user to:
#  - Add a new student
#  - Add grades for an existing student
#  - View the gradebook summary
#  - Allow the user to remove a student or a grade.
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
#- Print a clear summary of all students, their grades, and their average.
#- Display letter grades (A, B, C, etc.) based on averages.
#- Identify and print the student with the highest average.
highest_average = 0
best_student = ("")

for key, values in gradebook.items():
    letter_grade = ""
    average_score = sum(values) / len(values)
    if 100 >= average_score >= 90:
        letter_grade = "A"
    if 90 > average_score >= 80:
        letter_grade = "B"
    if 80 > average_score >= 70:
        letter_grade = "C"
    if 70 > average_score >= 60:
        letter_grade = "D"
    if average_score < 60:
        letter_grade = "F"
    print(key + ": " + str(values) + " Average: " + str(average_score) + " Letter Grade: " + letter_grade)
    if average_score > highest_average:
        highest_average = average_score 
        best_student = key

print()        
print("The student with the highest average score is " + best_student + ", with an average of " + str(highest_average) + "%")
print()
print("Students organized based on their averages (highest to lowest): ")
print()
#- Sort students by average grade.

avg_sorted = sorted(
    [(student, sum(grades) / len(grades)) for student, grades in gradebook.items()],
    key=lambda item: item[1],
    reverse=True,
)
for student, avg in avg_sorted:
    print(f"{student}'s Average : {avg:.2f}")
