age = int(input())
washer_price = float(input())
toy_price = int(input())

even_birth_day_count = 0
money_saved = 0

for year in range(1, age + 1):
    if year % 2 == 1:
        money_saved += toy_price
    else:
        even_birth_day_count += 1
        money_saved += 10 * even_birth_day_count
        money_saved -= 1

if money_saved >= washer_price:
    print(f"Yes! {money_saved - washer_price:.2f}")
else:
    print(f"No! {washer_price - money_saved:.2f}")
