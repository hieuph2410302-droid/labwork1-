num = int(input("Enter a number? "))
if num > 0:
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    if sum_divisors == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is a NOT perfect number")
else:
    print(f"{num} is a NOT perfect number")