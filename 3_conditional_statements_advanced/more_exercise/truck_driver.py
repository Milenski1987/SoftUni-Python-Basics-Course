TAX = 0.10
SEASON_LENGTH = 4

season = input()
kilometers_per_month = float(input())

money_earned_per_month = 0

if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        money_earned_per_month += kilometers_per_month * 0.75
    elif season == "Summer":
        money_earned_per_month += kilometers_per_month * 0.90
    elif season == "Winter":
        money_earned_per_month += kilometers_per_month * 1.05
elif kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        money_earned_per_month += kilometers_per_month * 0.95
    elif season == "Summer":
        money_earned_per_month += kilometers_per_month * 1.10
    elif season == "Winter":
        money_earned_per_month += kilometers_per_month * 1.25
elif kilometers_per_month <= 20000:
    money_earned_per_month += kilometers_per_month * 1.45

money_earned_per_season = (money_earned_per_month * SEASON_LENGTH) - ((money_earned_per_month * SEASON_LENGTH) * TAX)

print(f"{money_earned_per_season:.2f}")


