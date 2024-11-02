from math import floor

WINNER_POINTS = 2000
RUNNER_UP_POINTS = 1200
SEMI_FINALIST_POINTS = 720

number_of_tournaments = int(input())
starting_points = int(input())

earned_points = 0
win_count = 0

for tournament in range(number_of_tournaments):
    stage_reached = input()

    if stage_reached == "W":
        earned_points += WINNER_POINTS
        win_count += 1
    elif stage_reached == "F":
        earned_points += RUNNER_UP_POINTS
    elif stage_reached == "SF":
        earned_points += SEMI_FINALIST_POINTS

total_points = starting_points + earned_points
average_points = earned_points / number_of_tournaments
win_percent = (win_count / number_of_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_percent:.2f}%")


