SPRING_RENT = 3000
SUMMER_RENT = AUTUMN_RENT = 4200
WINTER_RENT = 2600

budget = int(input())
season = input()
number_of_fisherman = int(input())

total_cost = 0

if season == "Spring":
    total_cost = SPRING_RENT
    if number_of_fisherman <= 6:
        total_cost -= total_cost * 0.10
    elif 7 <= number_of_fisherman <= 11:
        total_cost -= total_cost * 0.15
    elif number_of_fisherman >= 12:
        total_cost -= total_cost * 0.25
elif season == "Summer" or season == "Autumn":
    total_cost = SUMMER_RENT
    if number_of_fisherman <= 6:
        total_cost -= total_cost * 0.10
    elif 7 <= number_of_fisherman <= 11:
        total_cost -= total_cost * 0.15
    elif number_of_fisherman >= 12:
        total_cost -= total_cost * 0.25
elif season == "Winter":
    total_cost = WINTER_RENT
    if number_of_fisherman <= 6:
        total_cost -= total_cost * 0.10
    elif 7 <= number_of_fisherman <= 11:
        total_cost -= total_cost * 0.15
    elif number_of_fisherman >= 12:
        total_cost -= total_cost * 0.25

if number_of_fisherman % 2 == 0 and season != "Autumn":
    total_cost -= total_cost * 0.05

money_diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Yes! You have {money_diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_diff:.2f} leva.")
