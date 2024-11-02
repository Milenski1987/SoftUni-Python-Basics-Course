fruit = input()
size_of_pack = input()
ordered_packs = int(input())

price_per_pack = 0

if size_of_pack == "small":
    if fruit == "Watermelon":
        price_per_pack += 56 * 2
    elif fruit == "Mango":
        price_per_pack += 36.66 * 2
    elif fruit == "Pineapple":
        price_per_pack += 42.10 * 2
    elif fruit == "Raspberry":
        price_per_pack += 20 * 2
elif size_of_pack == "big":
    if fruit == "Watermelon":
        price_per_pack += 28.70 * 5
    elif fruit == "Mango":
        price_per_pack += 19.60 * 5
    elif fruit == "Pineapple":
        price_per_pack += 24.80 * 5
    elif fruit == "Raspberry":
        price_per_pack += 15.20 * 5

total_sum = ordered_packs * price_per_pack

if 400 <= total_sum <= 1000:
    total_sum -= total_sum * 0.15
elif total_sum > 1000:
    total_sum -= total_sum * 0.50

print(f"{total_sum:.2f} lv.")