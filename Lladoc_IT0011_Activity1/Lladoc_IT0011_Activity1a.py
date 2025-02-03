num1, num2, num3 = map(float, input("Input three numbers separated by space: ").split())

if num1 >= num2 and num1 >= num3:
	highest = num1
elif num2 >= num1 and num2 >= num3:
	highest = num2
else:
	highest = num3

print(f"\nThe highest among the numbers you have entered is: \n{highest}")
