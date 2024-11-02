PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2
DISCOUNT = 0.25
RENT = 0.10

trip_price = float(input())
puzzle_quantity = int(input())
doll_quantity = int(input())
bear_quantity = int(input())
minion_quantity = int(input())
truck_quantity = int(input())

total_toys = puzzle_quantity + doll_quantity + bear_quantity + minion_quantity + truck_quantity
total_price = (puzzle_quantity * PUZZLE_PRICE) + (doll_quantity * DOLL_PRICE) \
              + (bear_quantity * BEAR_PRICE) + (minion_quantity * MINION_PRICE) \
              + (truck_quantity * TRUCK_PRICE)

if total_toys >= 50:
    total_price -= total_price * DISCOUNT

money_earned = total_price - (total_price * RENT)
money_diff = abs(money_earned - trip_price)

if money_earned >= trip_price:
    print(f"Yes! {money_diff:.2f} lv left.")
else:
    print(f"Not enough money! {money_diff:.2f} lv needed.")
