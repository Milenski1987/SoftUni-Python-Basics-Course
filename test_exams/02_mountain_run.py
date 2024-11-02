from math import floor

DELAY_PER_50M = 30

record = float(input())
distance = float(input())
time_per_1m = float(input())

total_delay = floor(distance / 50) * DELAY_PER_50M

total_time = (distance * time_per_1m) + total_delay

if total_time < record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time - record:.2f} seconds slower.")
