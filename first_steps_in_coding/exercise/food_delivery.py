CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGGIE_MENU = 8.15
DELIVERY = 2.50

quantity_chicken_menu = int(input())
quantity_fish_menu = int(input())
quantity_veggie_menu = int(input())

total_price = (quantity_veggie_menu * VEGGIE_MENU) \
              + (quantity_fish_menu * FISH_MENU) + (quantity_chicken_menu * CHICKEN_MENU)
dessert = total_price * 0.20

final_price = total_price + dessert + DELIVERY

print(final_price)


