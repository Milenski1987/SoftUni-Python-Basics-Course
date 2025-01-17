from math import ceil

COZ_PRICE = 4
EGG_PRICE = 0.45

number_of_guests = int(input())
budget = int(input())

eggs_needed = number_of_guests * 2
coz_needed = ceil(number_of_guests / 3)

money_needed = coz_needed * COZ_PRICE + eggs_needed * EGG_PRICE

if budget >= money_needed:
    print(f"Lyubo bought {coz_needed} Easter bread and {eggs_needed} eggs.")
    print(f"He has {budget - money_needed:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {money_needed - budget:.2f} lv. more.")
    