ROSE = 5
DAHLIA = 3.80
TULIP = 2.80
NARCISSUS = 3
GLADIOLUS = 2.50

type_of_flowers = input()
quantity_of_flowers = int(input())
budget = int(input())

total_price = 0

if type_of_flowers == "Roses":
    total_price = quantity_of_flowers * ROSE
    if quantity_of_flowers > 80:
        total_price -= total_price * 0.10
elif type_of_flowers == "Dahlias":
    total_price = quantity_of_flowers * DAHLIA
    if quantity_of_flowers > 90:
        total_price -= total_price * 0.15
elif type_of_flowers == "Tulips":
    total_price = quantity_of_flowers * TULIP
    if quantity_of_flowers > 80:
        total_price -= total_price * 0.15
elif type_of_flowers == "Narcissus":
    total_price = quantity_of_flowers * NARCISSUS
    if quantity_of_flowers < 120:
        total_price += total_price * 0.15
elif type_of_flowers == "Gladiolus":
    total_price = quantity_of_flowers * GLADIOLUS
    if quantity_of_flowers < 80:
        total_price += total_price * 0.20

money_diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {quantity_of_flowers} {type_of_flowers} and {money_diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_diff:.2f} leva more.")


