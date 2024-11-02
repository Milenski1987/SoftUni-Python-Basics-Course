TAXI_START_PRICE = 0.70
TAXI_DAY_PRICE = 0.79
TAXI_NIGHT_PRICE = 0.90
BUS_PRICE = 0.09
TRAIN_PRICE = 0.06

distance_to_be_travelled_in_km = int(input())
day_or_night_travel = input()

price = 0

if distance_to_be_travelled_in_km >= 100:
    price = distance_to_be_travelled_in_km * TRAIN_PRICE

elif distance_to_be_travelled_in_km >= 20:
    price = distance_to_be_travelled_in_km * BUS_PRICE

else:
    if day_or_night_travel == "day":
        price = (distance_to_be_travelled_in_km * TAXI_DAY_PRICE) + TAXI_START_PRICE
    elif day_or_night_travel == "night":
        price = (distance_to_be_travelled_in_km * TAXI_NIGHT_PRICE) + TAXI_START_PRICE

print(f"{price:.2f}")
