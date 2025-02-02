n = 7
num = 1

while num <= n:
    if num % 2 == 1 or num % 6 == 0:
        print(str(num) * num)
    num += 1
