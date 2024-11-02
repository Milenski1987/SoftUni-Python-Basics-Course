DISCOUNT_10_15 = 0.15
DISCOUNT_15_20 = 0.20
DISCOUNT_20_AND_MORE = 0.25

guests = int(input())
entry_fee_per_guest = float(input())
budget = float(input())

cake_price = budget * 0.10

if 10 <= guests <= 15:
    entry_fee_per_guest -= entry_fee_per_guest * DISCOUNT_10_15
elif 15 < guests <= 20:
    entry_fee_per_guest -= entry_fee_per_guest * DISCOUNT_15_20
elif guests > 20:
    entry_fee_per_guest -= entry_fee_per_guest * DISCOUNT_20_AND_MORE

entry_total_price = entry_fee_per_guest * guests

total_cost = entry_total_price + cake_price

if budget >= total_cost:
    print(f"It is party time! {budget - total_cost:.2f} leva left.")
else:
    print(f"No party! {total_cost - budget:.2f} leva needed.")
