from math import ceil

MOON_DISTANCE_FROM_EARTH = 384400
TIME_ON_MOON = 3


average_speed = float(input())
fuel_per_100_km = float(input())

total_distance = MOON_DISTANCE_FROM_EARTH * 2
time_for_total_distance = ceil(total_distance / average_speed)
total_time = time_for_total_distance + TIME_ON_MOON

fuel_needed = (fuel_per_100_km / 100) * total_distance

print(f"{total_time}\n{int(fuel_needed)}")
