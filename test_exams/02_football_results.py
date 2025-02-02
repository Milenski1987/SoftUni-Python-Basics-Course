first_game_result = input()
second_game_result = input()
third_game_result = input()

won_count = drawn_count = lost_count = 0

if first_game_result[0] > first_game_result[2]:
    won_count += 1
elif first_game_result[0] < first_game_result[2]:
    lost_count += 1
else:
    drawn_count += 1

if second_game_result[0] > second_game_result[2]:
    won_count += 1
elif second_game_result[0] < second_game_result[2]:
    lost_count += 1
else:
    drawn_count += 1

if third_game_result[0] > third_game_result[2]:
    won_count += 1
elif third_game_result[0] < third_game_result[2]:
    lost_count += 1
else:
    drawn_count += 1

print(f"Team won {won_count} games.")
print(f"Team lost {lost_count} games.")
print(f"Drawn games: {drawn_count}")
