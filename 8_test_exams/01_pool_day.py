from math import ceil

number_of_people = int(input())
entry_tax = float(input())
sun_lounger_price = float(input())
umbrella_price = float(input())

umbrellas_needed = ceil(number_of_people / 2)
sun_loungers_needed = ceil(number_of_people * 0.75)

total_cost = (number_of_people * entry_tax) + (umbrellas_needed * umbrella_price) \
             + (sun_loungers_needed * sun_lounger_price)

print(f"{total_cost:.2f} lv.")