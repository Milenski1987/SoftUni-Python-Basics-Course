food_purchased = int(input())
total_food_ate = 0

food_purchased_in_grams = food_purchased * 1000

while True:
    command = input()

    if command == "Adopted":
        break

    daily_food_ate = int(command)

    total_food_ate += daily_food_ate

diff = abs(food_purchased_in_grams - total_food_ate)
if total_food_ate <= food_purchased_in_grams:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
