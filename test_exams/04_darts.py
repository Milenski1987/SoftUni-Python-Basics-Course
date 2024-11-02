STARTING_POINTS = 301

player_name = input()
successful_shots_counter = 0
unsuccessful_shots_count = 0


while True:
    command = input()

    if command == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots_count} unsuccessful shots.")
        break

    points = int(input())
    turn_points = 0

    if command == "Single":
        turn_points += points
    elif command == "Double":
        turn_points += points * 2
    elif command == "Triple":
        turn_points += points * 3

    if STARTING_POINTS - turn_points < 0:
        unsuccessful_shots_count += 1
        continue
    elif STARTING_POINTS - turn_points == 0:
        successful_shots_counter += 1
        print(f"{player_name} won the leg with {successful_shots_counter} shots.")
        break
    else:
        STARTING_POINTS -= turn_points
        successful_shots_counter += 1

        
