first_name = input("Enter your first name: ") # this will prompt the user to input values
last_name = input("Enter your last name: ") # whatever string that is inputted here will be assigned to these variables

full_name = first_name + " " + last_name # this will concatenate the values assigned to the variables

upper_case_name = full_name.upper() # this function converts letters to uppercase 
lower_case_name = full_name.lower() # this function converts letters to lowercase

name_length = len(full_name) # this function calculates and counts the length of the string 

# Displaying the output together with the values
print("\nFull Name:", full_name)
print("Full Name (Upper Case):", upper_case_name)
print("Full Name (Lower Case):", lower_case_name)
print("Length of Full Name:", name_length)
