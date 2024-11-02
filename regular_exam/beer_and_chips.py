from math import ceil


BEER_PRICE = 1.20

name = input()
budget = float(input())
bottles_of_beer = int(input())
packages_of_chips = int(input())

packages_of_chips_price = (bottles_of_beer * BEER_PRICE) * 0.45

budget_needed = (bottles_of_beer * BEER_PRICE) + ceil(packages_of_chips * packages_of_chips_price)

budget_diff = abs(budget - budget_needed)

if budget >= budget_needed:
    print(f"{name} bought a snack and has {budget_diff:.2f} leva left." )
else:
    print(f"{name} needs {budget_diff:.2f} more leva!")
    