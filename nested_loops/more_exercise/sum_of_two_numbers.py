start_of_interval = int(input())
final_of_interval = int(input())
magic_number = int(input())

combinations_count = 0
magic_number_found = False

for x in range(start_of_interval, final_of_interval + 1):
    for y in range(start_of_interval, final_of_interval + 1):
        combinations_count += 1

        if x + y == magic_number:
            magic_number_found = True
            print(f"Combination N:{combinations_count} ({x} + {y} = {magic_number})")
            break

    if magic_number_found:
        break

else:
    print(f"{combinations_count} combinations - neither equals {magic_number}")



