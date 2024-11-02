budget = float(input())
money_spend = 0
products_counter = 0

while True:
    command = input()
    if command == "Stop":
        print(f"You bought {products_counter} products for {money_spend:.2f} leva.")
        break

    price_of_product = float(input())

    if (products_counter + 1) % 3 == 0:
        price_of_product -= price_of_product * 0.5

    if money_spend + price_of_product > budget:
        print("You don't have enough money!")
        print(f"You need {(abs(money_spend + price_of_product - budget)):.2f} leva!")
        break

    products_counter += 1
    money_spend += price_of_product

