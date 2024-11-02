PRICE_FOR_KG_CAT_FOOD = 12.45

number_of_cats = int(input())

group1_count = group2_count = group3_count = 0
total_food_eaten = 0

for _ in range(number_of_cats):
    food_eaten = float(input())

    if 100 <= food_eaten < 200:
        group1_count += 1
    elif 200 <= food_eaten < 300:
        group2_count += 1
    elif 300 <= food_eaten < 400:
        group3_count += 1

    total_food_eaten += food_eaten

food_price_per_day = f"{((total_food_eaten / 1000) * PRICE_FOR_KG_CAT_FOOD):.2f}"

print(f"Group 1: {group1_count} cats.")
print(f"Group 2: {group2_count} cats.")
print(f"Group 3: {group3_count} cats.")
print(f"Price for food per day: {food_price_per_day} lv.")

