projection = input()
package = input()
tickets = int(input())

bill = 0
ticket_price = 0

if projection == "John Wick":
    if package == "Drink":
        ticket_price += 12
    elif package == "Popcorn":
        ticket_price += 15
    elif package == "Menu":
        ticket_price += 19
elif projection == "Star Wars":
    if package == "Drink":
        ticket_price += 18
    elif package == "Popcorn":
        ticket_price += 25
    elif package == "Menu":
        ticket_price += 30
if projection == "Jumanji":
    if package == "Drink":
        ticket_price += 9
    elif package == "Popcorn":
        ticket_price += 11
    elif package == "Menu":
        ticket_price += 14

bill = tickets * ticket_price

if projection == "Star Wars" and tickets >= 4:
    bill -= bill * 0.30
if projection == "Jumanji" and tickets == 2:
    bill -= bill * 0.15

print(f"Your bill is {bill:.2f} leva.")
