import ast

# This is where the student data will be stored
students = [] 

# This function opens the file "student_records.txt" where the data is saved
def open_file(filename="student_records.txt"):
    global students
    try:
        with open(filename, "r") as file:
            students = [ast.literal_eval(line.strip()) for line in file.readlines()]
        print("File loaded successfully!")
    except FileNotFoundError: # I put exception handling for possible errors
        print("File not found. A new file will be created when you save.")

# This will save the records to the txt file
def save_file(filename="student_records.txt"):
    with open(filename, "w") as file:
        for student in students:
            file.write(str(student) + "\n")
    print("Records saved successfully!")

# This will display all the student records
def show_all_records(): # All the stored student records will be shown
    if not students:
        print("No records available.") # in case there are no records made yet
        return
    for student in students:
        print(student)

# This will sort the data on the order of their last name
def order_by_lastname():
    sorted_students = sorted(students, key=lambda x: x["name"][1])
    for student in sorted_students:
        print(student)

# This will sort the data on the order of their grades
def order_by_grade():
    sorted_students = sorted(students, key=lambda x: (x["class_standing"] * 0.6 + x["major_exam"] * 0.4), reverse=True)
    for student in sorted_students:
        print(student)

# This will only show a specific student record, the user will input their ID and the system will search through the stored values
def show_student_record(student_id):
    for student in students:
        if student["id"] == student_id:
            print(student)
            return
    print("Student not found!") # in case the student record is not found

# This function will add a student record to the file
def add_record(): # prompts the user to enter student details and adds the record to the file
    student_id = input("Enter 6-digit Student ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    students.append({"id": student_id, "name": (first_name, last_name), "class_standing": class_standing, "major_exam": major_exam})
    print("Record added successfully!")

# This function will edit an existing student record
def edit_record(student_id):
    for student in students:
        if student["id"] == student_id:
            student["name"] = (input("Enter New First Name: "), input("Enter New Last Name: "))
            student["class_standing"] = float(input("Enter New Class Standing Grade: "))
            student["major_exam"] = float(input("Enter New Major Exam Grade: "))
            print("Record updated successfully!")
            return
    print("Student not found!")

# This function will delete a student record
def delete_record(student_id):
    global students
    students = [student for student in students if student["id"] != student_id]
    print("Record deleted successfully!")

# MENU
def menu():
    while True: # menu based on the lab exercise instructions
        print("\nFEU TECH STUDENT RECORD MANAGEMENT\n")
        print("1. Open File")
        print("2. Save File")
        print("3. Show All Students Record")
        print("4. Order by Last Name")
        print("5. Order by Grade")
        print("6. Show Student Record")
        print("7. Add Record")
        print("8. Edit Record")
        print("9. Delete Record")
        print("10. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1": # the program will execute a specific condition based on the value inputted by the user
            open_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            show_all_records()
        elif choice == "4":
            order_by_lastname()
        elif choice == "5":
            order_by_grade()
        elif choice == "6":
            student_id = input("Enter Student ID: ")
            show_student_record(student_id)
        elif choice == "7":
            add_record()
        elif choice == "8":
            student_id = input("Enter Student ID to Edit: ")
            edit_record(student_id)
        elif choice == "9":
            student_id = input("Enter Student ID to Delete: ")
            delete_record(student_id)
        elif choice == "10":
            save_file()
            print("Exiting... Goodbye!")
            break
        else: # in case the inputted value is out of the choices
            print("Invalid choice! Please try again.")


menu()
