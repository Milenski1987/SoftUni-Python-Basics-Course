TOY_PRICE = 5
SWEATER_PRICE = 15

under_16years_count = over_16years_count = 0

while True:
    command = input()

    if command == "Christmas":
        break

    age = int(command)

    if age <= 16:
        under_16years_count += 1
    elif age > 16:
        over_16years_count += 1

money_for_toys = under_16years_count * TOY_PRICE
money_for_sweaters = over_16years_count * SWEATER_PRICE

print(f"Number of adults: {over_16years_count}")
print(f"Number of kids: {under_16years_count}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")
