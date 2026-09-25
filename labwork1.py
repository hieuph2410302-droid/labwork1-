# ==========================================
# ex1.py
# ==========================================
radius = float(input("Enter circle radius? "))
area = 3.14 * (radius ** 2)
print(f"Circle area = {area}")

# ==========================================
# ex2.py
# ==========================================
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = (celsius * 9/5) + 32
print(f"{int(celsius)} (C) = {fahrenheit} (F)")

# ==========================================
# ex3.py
# ==========================================
num = int(input("Enter a number? "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is a NOT prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is a NOT prime number")

# ==========================================
# ex4.py
# ==========================================
num = int(input("Enter a number? "))
if num > 0:
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    if sum_divisors == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is a NOT perfect number")
else:
    print(f"{num} is a NOT perfect number")

# ==========================================
# ex5.py
# ==========================================
colors = ['Blue', 'Yellow', 'Black', 'Red', 'White']
favorite_color = input("What is your favorite color? ")

if favorite_color in colors:
    index = colors.index(favorite_color)
    print(f"Your color is at index {index} in my list")
else:
    print("Sorry, I could not find your color")

# ==========================================
# ex6.py
# ==========================================
print("range1 |", ", ".join(map(str, range(7))))
print("range2 |", ", ".join(map(str, range(1, 13, 3))))
print("range3 |", ", ".join(map(str, range(5, 0, -1))))
print("range4 |", ", ".join(map(str, range(6, -3, -2))))

# ==========================================
# ex7.py
# ==========================================
def remove_dollar_sign(s):
    new_string = ""
    for char in s:
        if char != '$':
            new_string = new_string + char
    return new_string

result = remove_dollar_sign("The value is $100")
print(result)

# ==========================================
# ex8.py
# ==========================================
def extract_even(lst):
    even_numbers = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_numbers.append(lst[i])
    return even_numbers

original_list = [1, 4, 5, -1, 10]
print("Original list:", original_list)

result = extract_even(original_list)
print("List with only even numbers:", result)

# ==========================================
# ex9.py
# ==========================================
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

number = int(input("Enter a positive integer: "))
factorial = calculate_factorial(number)
print(f"The factorial of {number} is: {factorial}")

# ==========================================
# ex10.py
# ==========================================
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

# ==========================================
# ex11.py
# ==========================================
import math

def calculate_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx*dx + dy*dy)
    return distance

print("--- Enter coordinates for the first point ---")
point1_x = float(input("Enter x1: "))
point1_y = float(input("Enter y1: "))

print("--- Enter coordinates for the second point ---")
point2_x = float(input("Enter x2: "))
point2_y = float(input("Enter y2: "))

dist = calculate_distance(point1_x, point1_y, point2_x, point2_y)
print("The distance between the two points is:", dist)

# ==========================================
# ex12.py
# ==========================================
def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

print_pattern(4, 5)