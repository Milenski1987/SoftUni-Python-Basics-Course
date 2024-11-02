days = int(input())
hours_per_day = int(input())

total_tax = 0

for day in range(1, days + 1):
    money_to_be_paid = 0

    for hour in range(1, hours_per_day + 1):

        if day % 2 == 0 and hour % 2 != 0:
            money_to_be_paid += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            money_to_be_paid += 1.25
        else:
            money_to_be_paid += 1

    total_tax += money_to_be_paid
    print(f"Day: {day} - {money_to_be_paid:.2f} leva")


print(f"Total: {total_tax:.2f} leva")

