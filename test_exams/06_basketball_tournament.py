win_count = lose_count = games_count = 0

while True:
    tournament = input()

    if tournament == "End of tournaments":
        print(f"{(win_count / games_count * 100):.2f}% matches win")
        print(f"{(lose_count / games_count * 100):.2f}% matches lost")
        break

    number_of_games = int(input())

    for game in range(1, number_of_games + 1):
        games_count += 1
        desi_team_points = int(input())
        enemy_team_points = int(input())

        if desi_team_points > enemy_team_points:
            win_count += 1
            print(f"Game {game} of tournament {tournament}: win with {desi_team_points - enemy_team_points} points.")
        elif desi_team_points < enemy_team_points:
            lose_count += 1
            print(f"Game {game} of tournament {tournament}: lost with {enemy_team_points - desi_team_points} points.")
