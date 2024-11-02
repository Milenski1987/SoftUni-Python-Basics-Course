GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93
GASOLINE_DISCOUNT = 0.18
DIESEL_DISCOUNT = 0.12
GAS_DISCOUNT = 0.08
DISCOUNT_FOR_MORE_THAN_20_LITTERS = 0.08
DISCOUNT_FOR_MORE_THAN_25_LITTERS = 0.10

type_of_fuel = input()
amount_of_fuel = float(input())
club_card = input()

bill = 0

if type_of_fuel == "Gasoline":
    bill += amount_of_fuel * GASOLINE_PRICE
    if club_card == "Yes":
        bill -= amount_of_fuel * GASOLINE_DISCOUNT
elif type_of_fuel == "Diesel":
    bill += amount_of_fuel * DIESEL_PRICE
    if club_card == "Yes":
        bill -= amount_of_fuel * DIESEL_DISCOUNT
elif type_of_fuel == "Gas":
    bill += amount_of_fuel * GAS_PRICE
    if club_card == "Yes":
        bill -= amount_of_fuel * GAS_DISCOUNT

if amount_of_fuel > 25:
    bill -= bill * DISCOUNT_FOR_MORE_THAN_25_LITTERS
elif amount_of_fuel >= 20:
    bill -= bill * DISCOUNT_FOR_MORE_THAN_20_LITTERS

print(f"{bill:.2f} lv.")



