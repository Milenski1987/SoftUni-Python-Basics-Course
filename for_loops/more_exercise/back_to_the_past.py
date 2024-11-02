inherited_money = float(input())
year_to_live = int(input())

money_spend = 0

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        money_spend += 12000
    else:
        age = (year - 1800) + 18
        money_spend += 12000 + (50 * age)

money_diff = abs(inherited_money - money_spend)

if inherited_money >= money_spend:
    print(f"Yes! He will live a carefree life and will have {money_diff:.2f} dollars left.")
else:
    print(f"He will need {money_diff:.2f} dollars to survive.")
