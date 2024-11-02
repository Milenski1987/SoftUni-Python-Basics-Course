KOZUNAK = 3.20
EGGS_12_PIECES = 4.35
COOKIES = 5.40
EGG_PAINT_PER_EGG = 0.15

kozunak_quantity = int(input())
eggs_peels = int(input())
cookies_quantity = int(input())

kozunak_total_price = kozunak_quantity * KOZUNAK
eggs_total_price = (eggs_peels * EGGS_12_PIECES)
eggs_paint_price = (eggs_peels * 12) * 0.15
cookies_total_price = cookies_quantity * COOKIES

total_price = kozunak_total_price + eggs_total_price + cookies_total_price + eggs_paint_price

print(f"{total_price:.2f}")
