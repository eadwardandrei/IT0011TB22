def is_palindrome(n): # This will check if yung inputted value ay palindrome or not
    return str(n) == str(n)[::-1]

def check_sum_palindrome(filename): # This will read the 'numbers.txt' file and check if the sum of each line is a palindrome
    try: # This will open the file for reading
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            for i, line in enumerate(lines, start=1):
                try: # Macoconvert into a list of integers yung each line containing comma-separated values
                    numbers = list(map(int, line.strip().split(',')))
                    total = sum(numbers) # This will calculate the sum of the numbers in the line
                    
                    if is_palindrome(total): # If-else condition to check if a sum is a palindrome or not
                        print(f"Line {i}: {', '.join(map(str, numbers))} | Sum: {total}| --> It's a Palindrome!")
                    else:
                        print(f"Line {i}: {', '.join(map(str, numbers))} | Sum: {total} | --> It's not a Palindrome!")
                except ValueError:
                    print(f"Line {i}: Invalid data found!") # Error handling
                    
    except FileNotFoundError: # Error handling
        print(f"Error! The file '{filename}' was not found.")

check_sum_palindrome('numbers.txt')

