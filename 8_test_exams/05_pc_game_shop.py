games_sold = int(input())

hearthstone_count = fornite_count = overwatch_count = other_count = 0

for _ in range(games_sold):
    name_of_game = input()

    if name_of_game == "Hearthstone":
        hearthstone_count += 1
    elif name_of_game == "Fornite":
        fornite_count += 1
    elif name_of_game == "Overwatch":
        overwatch_count += 1
    else:
        other_count += 1

hearthstone_percent = hearthstone_count / games_sold * 100
fornite_percent = fornite_count / games_sold * 100
overwatch_percent = overwatch_count / games_sold * 100
others_percent = other_count / games_sold * 100

print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")

