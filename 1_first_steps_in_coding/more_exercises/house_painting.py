height_of_side = float(input())
length_of_side = float(input())
height_of_roof = float(input())

walls_area = ((2 * (height_of_side ** 2)) - (2 * 1.2)) + \
             ((2 * (height_of_side * length_of_side)) - 2 * (1.5 ** 2))

roof_area = (2 * (height_of_side * length_of_side)) + (2 * (height_of_side * height_of_roof / 2))

paint_for_walls = walls_area / 3.4
paint_for_roof = roof_area / 4.3

print(f"{paint_for_walls:.2f}")
print(f"{paint_for_roof:.2f}")

