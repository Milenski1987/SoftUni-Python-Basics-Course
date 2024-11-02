budget = float(input())
season = input()

location = ""
location_type = ""
vacation_cost = 0

if budget <= 1000:
    location_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        vacation_cost += budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        vacation_cost += budget * 0.45
elif budget <= 3000:
    location_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        vacation_cost += budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        vacation_cost += budget * 0.60
if budget > 3000:
    location_type = "Hotel"
    vacation_cost += budget * 0.90
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {location_type} - {vacation_cost:.2f}")

