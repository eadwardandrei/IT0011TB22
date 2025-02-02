input_string = input("Input a string that contains numbers: ")
digit_sum = 0

for char in input_string:
    if char.isdigit():
        digit_sum += int(char)

print(f"\nSum of digits: {digit_sum}")
