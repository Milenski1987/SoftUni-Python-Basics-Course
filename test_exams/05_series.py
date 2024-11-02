budget = float(input())
number_of_tv_series = int(input())
budget_needed = 0

for serial in range(number_of_tv_series):
    name_of_serial = input()
    price_for_serial = float(input())

    if name_of_serial == "Thrones":
        price_for_serial -= price_for_serial * 0.50
    elif name_of_serial == "Lucifer":
        price_for_serial -= price_for_serial * 0.40
    elif name_of_serial == "Protector":
        price_for_serial -= price_for_serial * 0.30
    elif name_of_serial == "TotalDrama":
        price_for_serial -= price_for_serial * 0.20
    elif name_of_serial == "Area":
        price_for_serial -= price_for_serial * 0.10

    budget_needed += price_for_serial

if budget >= budget_needed:
    print(f"You bought all the series and left with {(budget - budget_needed):.2f} lv.")
else:
    print(f"You need {(budget_needed - budget):.2f} lv. more to buy the series!")



