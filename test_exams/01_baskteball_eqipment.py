yearly_tax = int(input())

shoes_price = yearly_tax * 0.60
kit_price = shoes_price * 0.80
ball_price = kit_price / 4
accessories_price = ball_price / 5

total_price = yearly_tax + shoes_price + kit_price + ball_price + accessories_price

print(f"{total_price:.2f}")


