length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
free_volume = volume - (volume * (percent / 100))
water_in_liters = free_volume / 1000

print(water_in_liters)
