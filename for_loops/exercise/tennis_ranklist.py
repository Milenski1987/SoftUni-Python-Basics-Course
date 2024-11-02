from math import floor

WINNER = 2000
FINALIST = 1200
SEMI_FINALIST = 720

tournaments = int(input())
starting_rank_list_score = int(input())

points_earned = 0
won_count = 0

for _ in range(tournaments):
    stage = input()

    if stage == "W":
        points_earned += WINNER
        won_count += 1
    elif stage == "F":
        points_earned += FINALIST
    elif stage == "SF":
        points_earned += SEMI_FINALIST

total_score = starting_rank_list_score + points_earned

print(f"Final points: {total_score}")
print(f"Average points: {floor(points_earned / tournaments)}")
print(f"{(won_count / tournaments * 100):.2f}%")
