def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# --- Test the function ---
number = int(input("Enter an integer: "))
divisors_list = get_divisors(number)
print(f"All divisors of {number} are:", divisors_list)