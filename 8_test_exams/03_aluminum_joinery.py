DELIVERY = 60

number_of_joinery = int(input())
type_of_joinery = input()
type_of_delivery = input()

price = 0

if number_of_joinery <= 10:
    print("Invalid order")
else:
    if type_of_joinery == "90X130":
        price += 110
        if number_of_joinery > 60:
            price -= price * 0.08
        elif number_of_joinery > 30:
            price -= price * 0.05

    elif type_of_joinery == "100X150":
        price += 140
        if number_of_joinery > 80:
            price -= price * 0.10
        elif number_of_joinery > 40:
            price -= price * 0.06

    elif type_of_joinery == "130X180":
        price += 190
        if number_of_joinery > 50:
            price -= price * 0.12
        elif number_of_joinery > 20:
            price -= price * 0.07

    elif type_of_joinery == "200X300":
        price += 250
        if number_of_joinery > 50:
            price -= price * 0.14
        elif number_of_joinery > 25:
            price -= price * 0.09

    total_price = price * number_of_joinery

    if type_of_delivery == "With delivery":
        total_price += 60

    if number_of_joinery > 99:
        total_price -= total_price * 0.04

    print(f"{total_price:.2f} BGN")

