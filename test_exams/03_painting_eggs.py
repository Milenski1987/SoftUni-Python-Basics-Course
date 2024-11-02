egg_size = input()
egg_color = input()
batches = int(input())

batch_price = 0

if egg_size == "Large":
    if egg_color == "Red":
        batch_price += 16
    elif egg_color == "Green":
        batch_price += 12
    elif egg_color == "Yellow":
        batch_price += 9
elif egg_size == "Medium":
    if egg_color == "Red":
        batch_price += 13
    elif egg_color == "Green":
        batch_price += 9
    elif egg_color == "Yellow":
        batch_price += 7
elif egg_size == "Small":
    if egg_color == "Red":
        batch_price += 9
    elif egg_color == "Green":
        batch_price += 8
    elif egg_color == "Yellow":
        batch_price += 5

income = batches * batch_price
profit = income - (income * 0.35)

print(f"{profit:.2f} leva.")
