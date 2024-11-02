budget = float(input())
season = input()

type_of_journey = ""
destination = ""
spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_journey = "Camp"
        spent += budget * 0.30
    elif season == "winter":
        type_of_journey = "Hotel"
        spent += budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_journey = "Camp"
        spent += budget * 0.40
    elif season == "winter":
        type_of_journey = "Hotel"
        spent += budget * 0.80
elif budget > 1000:
    destination = "Europe"
    type_of_journey = "Hotel"
    spent += budget * 0.90

print(f"Somewhere in {destination}")
print(f"{type_of_journey} - {spent:.2f}")


