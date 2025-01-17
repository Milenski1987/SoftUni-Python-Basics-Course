football_team = input()
played_games = int(input())

points = wins_count = draw_count = lost_count = 0

if played_games < 1:
    print(f"{football_team} hasn't played any games during this season.")
else:
    for _ in range(played_games):
        result = input()

        if result == "W":
            wins_count += 1
            points += 3
        elif result == "D":
            draw_count += 1
            points += 1
        elif result == "L":
            lost_count += 1

    print(f"{football_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins_count}")
    print(f"## D: {draw_count}")
    print(f"## L: {lost_count}")
    print(f"Win rate: {(wins_count / played_games * 100):.2f}%")

