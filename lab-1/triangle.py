import math


def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))
print(f"The area of the triangle is: {calculate_triangle_area(a, b, c)}")
