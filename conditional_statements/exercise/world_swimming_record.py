from math import floor

DELAY = 12.5

record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter_in_seconds = float(input())

total_delay = floor(distance_in_meters / 15) * DELAY

total_time = distance_in_meters * time_per_meter_in_seconds + total_delay

if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_in_seconds:.2f} seconds slower.")

