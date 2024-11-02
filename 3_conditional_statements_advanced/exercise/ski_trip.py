ROOM_FOR_ONE_PERSON_PRICE = 18.00
APARTMENT_PRICE = 25.00
PRESIDENT_APARTMENT_PRICE = 35.00

days = int(input())
type_of_room = input()
evaluation = input()

nights = days - 1
total_cost = 0

if type_of_room == "room for one person":
    total_cost += nights * ROOM_FOR_ONE_PERSON_PRICE
elif type_of_room == "apartment":
    total_cost += nights * APARTMENT_PRICE
    if days < 10:
        total_cost -= total_cost * 0.30
    elif 10 <= days <= 15:
        total_cost -= total_cost * 0.35
    else:
        total_cost -= total_cost * 0.50
elif type_of_room == "president apartment":
    total_cost += nights * PRESIDENT_APARTMENT_PRICE
    if days < 10:
        total_cost -= total_cost * 0.10
    elif 10 <= days <= 15:
        total_cost -= total_cost * 0.15
    else:
        total_cost -= total_cost * 0.20

if evaluation == "positive":
    total_cost += total_cost * 0.25
elif evaluation == "negative":
    total_cost -= total_cost * 0.10

print(f"{total_cost:.2f}")
