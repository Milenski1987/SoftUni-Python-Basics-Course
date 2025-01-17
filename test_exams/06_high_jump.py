wanted_height_in_cm = int(input())
starting_height = wanted_height_in_cm - 30
jump_count = 0
fail_count = 0

while True:
    height_of_jump = int(input())
    jump_count += 1

    if height_of_jump <= starting_height:
        fail_count += 1

        if fail_count == 3:
            print(f"Tihomir failed at {starting_height}cm after {jump_count} jumps.")
            break

        continue

    else:
        fail_count = 0

        if starting_height >= wanted_height_in_cm:
            print(f"Tihomir succeeded, he jumped over {starting_height}cm after {jump_count} jumps.")
            break

        starting_height += 5
