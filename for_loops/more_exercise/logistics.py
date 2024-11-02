BUS = 200
TRUCK = 175
TRAIN = 120

number_of_cargos = int(input())

total_sum = 0
bus_tons = truck_tons = train_tons = 0

for _ in range(number_of_cargos):
    weight_in_tons = int(input())

    if weight_in_tons <= 3:
        total_sum += weight_in_tons * BUS
        bus_tons += weight_in_tons
    elif weight_in_tons <= 11:
        total_sum += weight_in_tons * TRUCK
        truck_tons += weight_in_tons
    elif weight_in_tons >= 12:
        total_sum += weight_in_tons * TRAIN
        train_tons += weight_in_tons

total_tons = bus_tons + truck_tons + train_tons
average_price_per_ton = total_sum / total_tons
bus_percent = bus_tons / total_tons * 100
truck_percent = truck_tons / total_tons * 100
train_percent = train_tons / total_tons * 100

print(f"{average_price_per_ton:.2f}")
print(f"{bus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")
