city = input()
pack = input()
vip = input()
days = int(input())

daily_price = 0
result = None

if city == "Bansko" or city == "Borovets":
    if days > 7:
        days -= 1
    if pack == "withEquipment":
        daily_price += 100
        if vip == "yes":
            daily_price -= daily_price * 0.10
        if days < 1:
            result = "Days must be positive number!"
        else:
            result = f"The price is {days * daily_price:.2f}lv! Have a nice time!"
    elif pack == "noEquipment":
        daily_price += 80
        if vip == "yes":
            daily_price -= daily_price * 0.05
        if days < 1:
            result = "Days must be positive number!"
        else:
            result = f"The price is {days * daily_price:.2f}lv! Have a nice time!"
    else:
        result = "Invalid input!"
elif city == "Varna" or city == "Burgas":
    if days > 7:
        days -= 1
    if pack == "withBreakfast":
        daily_price += 130
        if vip == "yes":
            daily_price -= daily_price * 0.12
        if days < 1:
            result = "Days must be positive number!"
        else:
            result = f"The price is {days * daily_price:.2f}lv! Have a nice time!"
    elif pack == "noBreakfast":
        daily_price += 100
        if vip == "yes":
            daily_price -= daily_price * 0.07
        if days < 1:
            result = "Days must be positive number!"
        else:
            result = f"The price is {days * daily_price:.2f}lv! Have a nice time!"
    else:
        result = "Invalid input!"
else:
    result = "Invalid input!"

print(result)
