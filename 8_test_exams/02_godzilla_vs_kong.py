DECOR_PRICE_PERCENT = 0.10
DISCOUNT_FOR_CLOTHES = 0.10

movie_budget = float(input())
number_of_spectators = int(input())
price_for_clothes = float(input())

decor_price = movie_budget * DECOR_PRICE_PERCENT
total_costs_for_clothes = number_of_spectators * price_for_clothes

if number_of_spectators > 150:
    total_costs_for_clothes -= total_costs_for_clothes * DISCOUNT_FOR_CLOTHES

budget_needed = decor_price + total_costs_for_clothes
budget_diff = abs(budget_needed - movie_budget)

if budget_needed > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {budget_diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget_diff:.2f} leva left.")
    