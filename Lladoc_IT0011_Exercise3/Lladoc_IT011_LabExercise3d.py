try: # this will open the file 'students.txt' in read mode
    with open("students.txt", "r") as file: # used the 'r' function to read the file
        student_info = file.read()
    
    # this will display the information in the file
    print("Reading Student Information...\n")
    print(student_info)

except FileNotFoundError: # in cases where the file does not exist, this condition will be executed
    print("Error: The file 'students.txt' was not found.")
