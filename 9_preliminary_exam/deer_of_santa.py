from math import floor, ceil

days_missing = int(input())
food_left = int(input())
first_deer_food_per_day = float(input())
second_deer_food_per_day = float(input())
third_deer_food_per_day = float(input())

total_food_per_day = first_deer_food_per_day + second_deer_food_per_day + third_deer_food_per_day
total_food_needed = total_food_per_day * days_missing

food_diff = abs(total_food_needed - food_left)

if food_left >= total_food_needed:
    print(f"{floor(food_diff)} kilos of food left.")
else:
    print(f"{ceil(food_diff)} more kilos of food are needed.")

