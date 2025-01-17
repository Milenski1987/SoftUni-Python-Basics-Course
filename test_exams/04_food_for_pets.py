days = int(input())
total_amount_of_food = float(input())

biscuits_amount = 0
dog_food_eaten = cat_food_eaten = 0

for day in range(1, days + 1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())

    dog_food_eaten += food_eaten_by_dog
    cat_food_eaten += food_eaten_by_cat

    if day % 3 == 0:
        biscuits_amount += (food_eaten_by_cat + food_eaten_by_dog) * 0.10

total_food_eaten = dog_food_eaten + cat_food_eaten
eaten_food_percent = (total_food_eaten / total_amount_of_food) * 100
dog_percent = dog_food_eaten / total_food_eaten * 100
cat_percent = cat_food_eaten / total_food_eaten * 100

print(f"Total eaten biscuits: {round(biscuits_amount)}gr.\n{eaten_food_percent:.2f}% "
      f"of the food has been eaten.\n{dog_percent:.2f}% eaten from the dog.\n{cat_percent:.2f}% eaten from the cat.")


