DISCOUNT_BILL = 0.25

profit_wanted = float(input())
money_earned = 0
result = None

while True:
    command = input()

    if command == "Party!":
        result = f"We need {profit_wanted - money_earned:.2f} leva more."
        break

    number_of_cocktails = int(input())

    cocktail_price = len(command)

    if (number_of_cocktails * cocktail_price) % 2 != 0:
        money_earned += (number_of_cocktails * cocktail_price) - (number_of_cocktails * cocktail_price * DISCOUNT_BILL)
    else:
        money_earned += (number_of_cocktails * cocktail_price)

    if money_earned >= profit_wanted:
        result = "Target acquired."
        break

print(result)
print(f"Club income - {money_earned:.2f} leva.")
