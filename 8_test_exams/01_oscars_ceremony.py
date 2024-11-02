hall_rent = int(input())

statues_price = hall_rent * 0.70
catering_price = statues_price * 0.85
sound_price = catering_price / 2

costs = hall_rent + statues_price + catering_price + sound_price

print(f"{costs:.2f}")

