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