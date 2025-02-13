from datetime import datetime

def format_date():
    
    while True: # This will ask the user to input a date or to exit the program
        date_str = input("\nEnter a date (MM/DD/YYYY) or type 'exit' to quit: ")
        if date_str.lower() == 'exit': # This condition will be executed if the user wants to exit
            print("Goodbye!")
            break
        
        try: # This will convert the inputted date to a datetime object
            date_obj = datetime.strptime(date_str, "%m/%d/%Y")
            formatted_date = date_obj.strftime("%B %d, %Y") # Mafformat na yung datetime object into a human-readable string
            print("Date Output:", formatted_date)
            
        except ValueError: # Error handling 
            print("Invalid date format! Please use this format: MM/DD/YYYY.")

format_date()
