num = int(input("Input a number: "))

if num == 0 or num == 1:
    print(f"\n{num} is not a prime number!")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(f"\n{num} is not a prime number!")
           print(f"{i} times",num//i, f"is {num}.")
           break
   else:
       print(f"\n{num} is a prime number!")
else:
   print(f"\n{num} is not a prime number!")
