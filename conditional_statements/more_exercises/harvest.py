from math import floor, ceil

PERCENT_FOR_WINE_PRODUCTION = 0.40
LITER_WINE_GRAPE_NEEDED = 2.5

area = int(input())
grapes_per_sq_m = float(input())
needed_liters_wine = int(input())
number_of_workers = int(input())

area_for_wine_production = area * PERCENT_FOR_WINE_PRODUCTION
grapes_gathered = area_for_wine_production * grapes_per_sq_m
liters_wine_produced = grapes_gathered / LITER_WINE_GRAPE_NEEDED
liters_dif = abs(needed_liters_wine - liters_wine_produced)

if liters_wine_produced < needed_liters_wine:
    print(f"It will be a tough winter! More {floor(liters_dif)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(liters_wine_produced)} liters.")
    print(f"{ceil(liters_dif)} liters left -> {ceil(liters_dif / number_of_workers)} liters per person.")




