TICKET_PRICE = 5

hall_capacity = int(input())
money_earned = 0
full = False

while True:
    command = input()

    if command == "Movie time!":
        print(f"There are {hall_capacity} seats left in the cinema.")
        break

    if (hall_capacity - int(command)) < 0:
        full = True
        break

    hall_capacity -= int(command)

    if int(command) % 3 == 0:
        money_earned += (int(command) * TICKET_PRICE) - 5
    else:
        money_earned += int(command) * TICKET_PRICE

if full:
    print(f"The cinema is full.")

print(f"Cinema income - {money_earned} lv.")


