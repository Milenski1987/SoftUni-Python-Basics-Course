sweet = input()
sweet_quantity = int(input())
day_of_december = int(input())

sweet_price = 0

if day_of_december <= 15:
    if sweet == "Cake":
        sweet_price += 24
    elif sweet == "Souffle":
        sweet_price += 6.66
    elif sweet == "Baklava":
        sweet_price += 12.60

elif 15 < day_of_december < 25:
    if sweet == "Cake":
        sweet_price += 28.70
    elif sweet == "Souffle":
        sweet_price += 9.80
    elif sweet == "Baklava":
        sweet_price += 16.98

total_price = sweet_quantity * sweet_price

if day_of_december <= 22:
    if 100 <= total_price <= 200:
        total_price -= total_price * 0.15
    elif total_price > 200:
        total_price -= total_price * 0.25

if day_of_december <= 15:
    total_price -= total_price * 0.10

print(f"{total_price:.2f}")



