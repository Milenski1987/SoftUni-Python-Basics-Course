FUEL_PRICE_FOR_LITER = 2.10
GUIDE_PRICE = 100
SATURDAY_DISCOUNT = 0.10
SUNDAY_DISCOUNT = 0.20

budget = float(input())
fuel_needed = float(input())
day_of_the_week = input()
discount = 0

if day_of_the_week == "Saturday":
    discount = SATURDAY_DISCOUNT
elif day_of_the_week == "Sunday":
    discount = SUNDAY_DISCOUNT

money_needed = ((fuel_needed * FUEL_PRICE_FOR_LITER) + GUIDE_PRICE) * (1 - discount)

if money_needed <= budget:
    print(f"Safari time! Money left: {(budget - money_needed):.2f} lv.")
else:
    print(f"Not enough money! Money needed: {(money_needed - budget):.2f} lv.")