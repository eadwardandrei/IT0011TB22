last_name = input("Enter last name: ") # this will get the last name of the user
first_name = input("Enter first name: ") # this will get the first name of the user
age = input("Enter age: ") # this will get the age of the user
contact_number = input("Enter contact number: ") # this will get the contact number of the user
course = input("Enter program: ") # this will get the program of the user

# this is so that the details will be formatted properly 
student_info = f"Last Name: {last_name}\nFirst Name: {first_name}\nAge: {age}\nContact Number: {contact_number}\nCourse: {course}\n\n"

with open("students.txt", "a") as file: # this function will make the file in append mode to input the information
    file.write(student_info)

# this will display to confirm if data inputted by the user has been saved
print("Student information has been saved to 'students.txt'.")
