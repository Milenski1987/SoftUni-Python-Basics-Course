budget = float(input())
destination = input()
season = input()
days = int(input())

budget_needed = 0
daily_price = 0

if season == "Winter":
    if destination == "Dubai":
        daily_price += 45000
    elif destination == "Sofia":
        daily_price += 17000
    elif destination == "London":
        daily_price += 24000
elif season == "Summer":
    if destination == "Dubai":
        daily_price += 40000
    elif destination == "Sofia":
        daily_price += 12500
    elif destination == "London":
        daily_price += 20250

budget_needed += days * daily_price

if destination == "Dubai":
    budget_needed -= budget_needed * 0.30
elif destination == "Sofia":
    budget_needed += budget_needed * 0.25

budget_diff = abs(budget - budget_needed)

if budget >= budget_needed:
    print(f"The budget for the movie is enough! We have {budget_diff:.2f} leva left!")
else:
    print(f"The director needs {budget_diff:.2f} leva more!")
    