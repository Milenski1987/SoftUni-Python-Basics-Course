from math import ceil

wall_height = int(input())
wall_width = int(input())
percent_not_be_painted = int(input())

area_to_be_painted = wall_height * wall_width * 4
percent_in_area = area_to_be_painted * (percent_not_be_painted / 100)
total_to_painting = ceil(area_to_be_painted - percent_in_area)

paint_left = 0

while True:
    command = input()

    if command == "Tired!":
        print(f"{total_to_painting} quadratic m left.")
        break

    liters_paint = int(command)
    paint_left = abs(total_to_painting - liters_paint)
    total_to_painting -= liters_paint

    if total_to_painting <= 0:
        if paint_left == 0:
            print("All walls are painted! Great job, Pesho!")
        else:
            print(f"All walls are painted and you have {paint_left} l paint left!")
        break

