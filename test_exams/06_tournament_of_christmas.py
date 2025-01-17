days_of_tournament = int(input())

money_won = 0
days_win = days_lost = 0

for day in range(days_of_tournament):
    daily_money_earned = 0
    games_won = games_lost = 0

    while True:
        command = input()

        if command == "Finish":
            break

        result = input()

        if result == "win":
            games_won += 1
            daily_money_earned += 20
        elif result == "lose":
            games_lost += 1

    if games_won > games_lost:
        days_win += 1
        money_won += daily_money_earned + (daily_money_earned * 0.10)
    elif games_won < games_lost:
        days_lost += 1
        money_won += daily_money_earned

if days_win > days_lost:
    money_won += money_won * 0.20
    print(f"You won the tournament! Total raised money: {money_won:.2f}")
elif days_lost > days_win:
    print(f"You lost the tournament! Total raised money: {money_won:.2f}")
