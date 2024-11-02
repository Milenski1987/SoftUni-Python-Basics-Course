NIGHTS_DISCOUNT_PERCENT = 0.05

budget = float(input())
nights = int(input())
night_price = float(input())
additional_costs_percent = int(input())

if nights > 7:
    night_price -= night_price * NIGHTS_DISCOUNT_PERCENT

money_needed = (budget * (additional_costs_percent / 100)) + (nights * night_price)

if budget >= money_needed:
    print(f"Ivanovi will be left with {budget - money_needed:.2f} leva after vacation.")
else:
    print(f"{money_needed - budget:.2f} leva needed.")
    