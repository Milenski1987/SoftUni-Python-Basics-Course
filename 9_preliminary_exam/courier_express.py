shipment_weight = float(input())
type_of_service = input()
distance_in_km = int(input())

price_per_km = 0
additional_cost_percent = 0
additional_cost = 0

if 0 < shipment_weight < 1:
    price_per_km += 0.03
elif 1 <= shipment_weight < 10:
    price_per_km += 0.05
elif 10 <= shipment_weight < 40:
    price_per_km += 0.10
elif 40 <= shipment_weight < 90:
    price_per_km += 0.15
elif 90 <= shipment_weight < 150:
    price_per_km += 0.20

shipment_cost = distance_in_km * price_per_km

if type_of_service == "express":
    if 0 < shipment_weight < 1:
        additional_cost_percent += 0.80
    elif 1 <= shipment_weight < 10:
        additional_cost_percent += 0.40
    elif 10 <= shipment_weight < 40:
        additional_cost_percent += 0.05
    elif 40 <= shipment_weight < 90:
        additional_cost_percent += 0.02
    elif 90 <= shipment_weight < 150:
        additional_cost_percent += 0.01

    additional_cost = ((additional_cost_percent * price_per_km) * shipment_weight) * distance_in_km

total_shipment_cost = shipment_cost + additional_cost

print(f"The delivery of your shipment with weight of {shipment_weight:.3f} kg. would cost {total_shipment_cost:.2f} lv.")
