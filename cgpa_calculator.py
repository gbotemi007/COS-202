print("===========================================")
print("      PERSONAL POCKET CGPA CALCULATOR")
print("===========================================")

print("1. Calculate Semester GPA")
print("2. Calculate New CGPA")

choice = input("Enter your choice (1 or 2): ")

# ------------------ OPTION 1 ------------------
if choice == "1":

    number_of_courses = int(input("\nHow many courses did you offer? "))

    total_units = 0
    total_grade_points = 0

    for i in range(number_of_courses):

        print("\nCourse", i + 1)

        course_code = input("Enter Course Code: ")
        course_unit = int(input("Enter Course Unit: "))
        grade = input("Enter Grade (A, B, C, D, E, F): ").upper()

        if grade == "A":
            point = 5
        elif grade == "B":
            point = 4
        elif grade == "C":
            point = 3
        elif grade == "D":
            point = 2
        elif grade == "E":
            point = 1
        elif grade == "F":
            point = 0
        else:
            print("Invalid Grade!")
            continue

        grade_point = point * course_unit

        print("Grade Point Earned =", grade_point)

        total_units = total_units + course_unit
        total_grade_points = total_grade_points + grade_point

    gpa = total_grade_points / total_units

    print("\n===========================================")
    print("SEMESTER GPA RESULT")
    print("===========================================")
    print("Total Units =", total_units)
    print("Total Grade Points =", total_grade_points)
    print("Semester GPA =", round(gpa, 2))

# ------------------ OPTION 2 ------------------
elif choice == "2":

    previous_cgpa = float(input("\nEnter Previous CGPA: "))
    previous_units = int(input("Enter Previous Total Units: "))

    number_of_courses = int(input("How many courses did you offer this semester? "))

    semester_units = 0
    semester_grade_points = 0

    for i in range(number_of_courses):

        print("\nCourse", i + 1)

        course_code = input("Enter Course Code: ")
        course_unit = int(input("Enter Course Unit: "))
        grade = input("Enter Grade (A, B, C, D, E, F): ").upper()

        if grade == "A":
            point = 5
        elif grade == "B":
            point = 4
        elif grade == "C":
            point = 3
        elif grade == "D":
            point = 2
        elif grade == "E":
            point = 1
        elif grade == "F":
            point = 0
        else:
            print("Invalid Grade!")
            continue

        grade_point = point * course_unit

        print("Grade Point Earned =", grade_point)

        semester_units = semester_units + course_unit
        semester_grade_points = semester_grade_points + grade_point

    semester_gpa = semester_grade_points / semester_units

    previous_grade_points = previous_cgpa * previous_units

    new_total_grade_points = previous_grade_points + semester_grade_points
    new_total_units = previous_units + semester_units

    new_cgpa = new_total_grade_points / new_total_units

    print("\n===========================================")
    print("NEW CGPA RESULT")
    print("===========================================")
    print("Previous CGPA =", previous_cgpa)
    print("Previous Units =", previous_units)
    print("Current Semester GPA =", round(semester_gpa, 2))
    print("New CGPA =", round(new_cgpa, 2))

# ------------------ INVALID OPTION ------------------
else:
    print("Invalid Choice!")