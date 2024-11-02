NO_SUGAR_DRINK_DISCOUNT = 0.35
ESPRESSO_MORE_THAN_5_DISCOUNT = 0.25
BILL_MORE_THAN_15_DISCOUNT = 0.20

drink = input()
sugar = input()
number_of_drinks = int(input())

bill = 0

if drink == "Espresso":
    if sugar == "Without":
        bill += number_of_drinks * 0.90
    elif sugar == "Normal":
        bill += number_of_drinks * 1
    elif sugar == "Extra":
        bill += number_of_drinks * 1.20
if drink == "Cappuccino":
    if sugar == "Without":
        bill += number_of_drinks * 1.00
    elif sugar == "Normal":
        bill += number_of_drinks * 1.20
    elif sugar == "Extra":
        bill += number_of_drinks * 1.60
if drink == "Tea":
    if sugar == "Without":
        bill += number_of_drinks * 0.50
    elif sugar == "Normal":
        bill += number_of_drinks * 0.60
    elif sugar == "Extra":
        bill += number_of_drinks * 0.70

if sugar == "Without":
    bill -= bill * NO_SUGAR_DRINK_DISCOUNT
if drink == "Espresso" and number_of_drinks >= 5:
    bill -= bill * ESPRESSO_MORE_THAN_5_DISCOUNT
if bill > 15:
    bill -= bill * BILL_MORE_THAN_15_DISCOUNT

print(f"You bought {number_of_drinks} cups of {drink} for {bill:.2f} lv.")

