month = input()
nights = int(input())

studio_total_cost = 0
apartment_total_cost = 0

if month == "May" or month == "October":
    studio_total_cost = nights * 50
    apartment_total_cost = nights * 65
    if nights > 14:
        studio_total_cost -= studio_total_cost * 0.30
        apartment_total_cost -= apartment_total_cost * 0.10
    elif nights > 7:
        studio_total_cost -= studio_total_cost * 0.05
elif month == "June" or month == "September":
    studio_total_cost = nights * 75.20
    apartment_total_cost = nights * 68.70
    if nights > 14:
        studio_total_cost -= studio_total_cost * 0.20
        apartment_total_cost -= apartment_total_cost * 0.10
elif month == "July" or month == "August":
    studio_total_cost = nights * 76
    apartment_total_cost = nights * 77
    if nights > 14:
        apartment_total_cost -= apartment_total_cost * 0.10

print(f"Apartment: {apartment_total_cost:.2f} lv.")
print(f"Studio: {studio_total_cost:.2f} lv.")


