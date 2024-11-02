from math import pi

figure_type = input()
area = 0

if figure_type == "square":
    side_length = float(input())
    area = side_length ** 2
elif figure_type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure_type == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
elif figure_type == "triangle":
    side_length = float(input())
    height = float(input())
    area = side_length * (height / 2)

print(f"{area:.3f}")

