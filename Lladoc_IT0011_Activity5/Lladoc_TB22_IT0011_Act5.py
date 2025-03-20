def divide(a, b): # division, it will return the result devided by b, ensuring b is not zero
    if b == 0: 
        print("Error! Division by zero is not allowed.")
        return None
    return a / b 

def exponentiate(a, b):
    return a ** b # this returns a raised to the power of b

def remainder(a, b):
    if b == 0: # returns the remainder of a divided by b, ensuring b is not zero
        print("Error! Division by zero is not allowed.")
        return None
    return a % b

def summation(a, b): 
    if a > b: # returns the sum of all numbers from a to b, ensuring b is greater than a
        print("Error! The second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))

def main(): # displays the menu and handles user input for mathematical operations
    while True:
        print("\nEADWARD's MATHEMATICAL OPERATIONS MENU")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("\nEnter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("\nExiting the program. Have a nice day!")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = float(input("Input the first value: "))
                num2 = float(input("Input the second value: "))
                
                if choice == 'D':
                    result = divide(num1, num2)
                elif choice == 'E':
                    result = exponentiate(num1, num2)
                elif choice == 'R':
                    result = remainder(num1, num2)
                elif choice == 'F':
                    result = summation(int(num1), int(num2))
                
                if result is not None:
                    print("Result:", result)
            except ValueError:
                print("Error! Please enter valid numbers.")
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
