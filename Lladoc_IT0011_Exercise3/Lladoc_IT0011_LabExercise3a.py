first_name = input("Enter your first name: ")# This will ask the user to input values
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

full_name = first_name + " " + last_name # The concatenated names will be assigned to this variable

sliced_name = first_name[:3]  # This function will then slice the first name and get the first three characters

# The message will be assigned to this variable so that when it is called out, it will display it.
# The age will also display depending on the value inputted by the user
greeting_message = f"Hello, {sliced_name}! Welcome. You are {age} years old."

# Output will be displayed with these prompts
print("\nFull Name:", full_name)
print("Sliced Name:", sliced_name)
print("Greeting Message:", greeting_message)
