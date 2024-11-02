width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

free_volume = width_free_space * length_free_space * height_free_space

while free_volume > 0:
    command = input()

    if command == "Done":
        print(f"{free_volume} Cubic meters left.")
        break

    boxes = int(command)
    free_volume -= boxes

else:
    print(f"No more free space! You need {abs(free_volume)} Cubic meters more.")

