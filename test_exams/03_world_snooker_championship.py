stage_of_tournament = input()
type_of_ticket = input()
tickets = int(input())
photo_with_trophy = input()

ticket_price = 0
free_photo = False

if stage_of_tournament == "Quarter final":
    if type_of_ticket == "Standard":
        ticket_price += 55.50
    elif type_of_ticket == "Premium":
        ticket_price += 105.20
    elif type_of_ticket == "VIP":
        ticket_price += 118.90
elif stage_of_tournament == "Semi final":
    if type_of_ticket == "Standard":
        ticket_price += 75.88
    elif type_of_ticket == "Premium":
        ticket_price += 125.22
    elif type_of_ticket == "VIP":
        ticket_price += 300.40
elif stage_of_tournament == "Final":
    if type_of_ticket == "Standard":
        ticket_price += 110.10
    elif type_of_ticket == "Premium":
        ticket_price += 160.66
    elif type_of_ticket == "VIP":
        ticket_price += 400

total_price = tickets * ticket_price

if total_price > 4000:
    total_price -= total_price * 0.25
    free_photo = True
elif total_price > 2500:
    total_price -= total_price * 0.10

if photo_with_trophy == "Y" and not free_photo:
    total_price += tickets * 40

print(f"{total_price:.2f}")
        