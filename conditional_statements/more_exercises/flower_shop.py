from math import floor, ceil

MAGNOLIAS_PRICE = 3.25
HYACINTHS_PRICE = 4
ROSES_PRICE = 3.50
CACTUS_PRICE = 8
TAX = 0.05

magnolias_quantity = int(input())
hyacinths_quantity = int(input())
roses_quantity = int(input())
cactus_quantity = int(input())
gift_price = float(input())

sales = (magnolias_quantity * MAGNOLIAS_PRICE) + (hyacinths_quantity * HYACINTHS_PRICE) \
        + (roses_quantity * ROSES_PRICE) + (cactus_quantity * CACTUS_PRICE)

profit = sales - (sales * TAX)
diff = abs(profit - gift_price)

if profit >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")

