number_of_painted_eggs = int(input())

red_count = orange_count = blue_count = green_count = 0
most_eggs_color = ""
most_eggs = 0

for egg in range(number_of_painted_eggs):
    egg_color = input()

    if egg_color == "red":
        red_count += 1
    elif egg_color == "orange":
        orange_count += 1
    elif egg_color == "blue":
        blue_count += 1
    elif egg_color == "green":
        green_count += 1

most_eggs_color = "red"
most_eggs = red_count

if orange_count > most_eggs:
    most_eggs_color = "orange"
    most_eggs = orange_count
if blue_count > most_eggs:
    most_eggs_color = "blue"
    most_eggs = blue_count
if green_count > most_eggs:
    most_eggs_color = "green"
    most_eggs = green_count

print(f"Red eggs: {red_count}")
print(f"Orange eggs: {orange_count}")
print(f"Blue eggs: {blue_count}")
print(f"Green eggs: {green_count}")
print(f"Max eggs: {most_eggs} -> {most_eggs_color}")

