from math import floor, ceil

tennis_racket_price = float(input())
tennis_rackets_quantity = int(input())
shoes_quantity = int(input())

shoes_price = tennis_racket_price / 6

equipment_price = (tennis_racket_price * tennis_rackets_quantity) + (shoes_price * shoes_quantity)
additional_equipment = equipment_price * 0.20

total_equipment_cost = equipment_price + additional_equipment

player_price = total_equipment_cost / 8
sponsor_price = (total_equipment_cost * 7) / 8

print(f"Price to be paid by Djokovic {floor(player_price)}")
print(f"Price to be paid by sponsors {ceil(sponsor_price)}")

