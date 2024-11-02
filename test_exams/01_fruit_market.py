strawberry_price = float(input())
bananas_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price * 0.60
bananas_price = raspberry_price * 0.20

total_price = (strawberry_price * strawberry_quantity) \
              + (bananas_price * bananas_quantity) \
              + (orange_price * orange_quantity) + (raspberry_quantity * raspberry_price)

print(f"{total_price:.2f}")

