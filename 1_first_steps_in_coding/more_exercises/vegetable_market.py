vegetables_price = float(input())
fruits_price = float(input())
vegetables_quantity = int(input())
fruits_quantity = int(input())

price_in_euro = ((vegetables_price * vegetables_quantity) + (fruits_quantity * fruits_price)) / 1.94

print(f"{price_in_euro:.2f}")