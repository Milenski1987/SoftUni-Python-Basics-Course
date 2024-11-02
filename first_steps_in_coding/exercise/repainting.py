PRICE_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_THINNER = 5.00
PRICE_BAGS = 0.40

needed_nylon = int(input())
needed_paint = int(input())
amount_thinner = int(input())
hours_to_be_done = int(input())

total_price_nylon = (needed_nylon + 2) * PRICE_NYLON
total_price_paint = (needed_paint + (needed_paint * 0.10)) * PRICE_PAINT
total_price_thinner = amount_thinner * PRICE_THINNER
total_price_materials = total_price_thinner + total_price_paint + total_price_nylon + PRICE_BAGS
price_for_workers = (total_price_materials * 0.30) * hours_to_be_done
final_price = total_price_materials + price_for_workers

print(final_price)
