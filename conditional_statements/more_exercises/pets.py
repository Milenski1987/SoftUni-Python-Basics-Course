from math import floor, ceil

days = int(input())
food_in_storage = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

turtle_food_in_kg = turtle_food_per_day / 1000

food_needed = (dog_food_per_day + cat_food_per_day + turtle_food_in_kg) * days
food_diff = abs(food_in_storage - food_needed)

if food_in_storage >= food_needed:
    print(f"{floor(food_diff)} kilos of food left.")
else:
    print(f"{ceil(food_diff)} more kilos of food are needed.")
