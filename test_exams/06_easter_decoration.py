EGG_BASKET = 1.50
EASTER_WREATH = 3.80
CHOCOLATE_BUNNY = 7

number_of_customers = int(input())
total_money_spend = 0

for customer in range(number_of_customers):
    purchases = 0
    price = 0
    while True:
        command = input()

        if command == "Finish":
            if purchases % 2 == 0:
                price -= price * 0.20
            print(f"You purchased {purchases} items for {price:.2f} leva.")
            break
        elif command == "basket":
            purchases += 1
            price += EGG_BASKET
        elif command == "wreath":
            purchases += 1
            price += EASTER_WREATH
        elif command == "chocolate bunny":
            purchases += 1
            price += CHOCOLATE_BUNNY

    total_money_spend += price

print(f"Average bill per client is: {total_money_spend / number_of_customers:.2f} leva.")
