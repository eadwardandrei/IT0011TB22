r = int(input("Enter first term number: "))
n = int(input("Enter second term number: ")) 
sum = 0 
for i in range(r, n+1): 
  sum += i 
print(f"The sum of the numbers from {r} to {n} is:", sum) 
