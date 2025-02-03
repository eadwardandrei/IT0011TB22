num1, num2, num3 = map(float, input("Input three numbers separated by space: ").split())

if num1 >= num2 and num1 >= num3:
	highest = num1
	if num2 >= num3:
		middle, lowest = num2, num3
	else:
		middle, lowest = num3, num2
elif num2 >= num1 and num2 >= num3:
	highest = num2
	if num1 >= num3:
		middle, lowest = num1, num3
	else:
		middle, lowest = num3, num1
else:
	highest = num3
	if num1 >= num2:
		middle, lowest = num1, num2
	else: 
		middle, lowest = num2, num1

print(f"From highest to lowest: \n{highest}, \n{middle}, \n{lowest}")
