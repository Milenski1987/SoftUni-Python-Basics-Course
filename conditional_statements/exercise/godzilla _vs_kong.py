MOVIE_DECOR_PERCENT = 0.10
DISCOUNT_FOR_SPECTATORS = 0.10

movie_budget = float(input())
number_of_spectators = int(input())
price_for_spectator_cloth = float(input())

decor_price = movie_budget * MOVIE_DECOR_PERCENT

if number_of_spectators > 150:
    price_for_spectator_cloth -= price_for_spectator_cloth * DISCOUNT_FOR_SPECTATORS

total_spectator_cloth_price = number_of_spectators * price_for_spectator_cloth

budget_needed = decor_price + total_spectator_cloth_price

if budget_needed > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {budget_needed - movie_budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - budget_needed:.2f} leva left.")
