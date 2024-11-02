JUNIORS_TRAIL_TAX = 5.50
JUNIORS_CROSS_COUNTRY_TAX = 8
JUNIORS_DOWNHILL_TAX = 12.25
JUNIORS_ROAD_TAX = 20

SENIORS_TRAIL_TAX = 7
SENIORS_CROSS_COUNTRY_TAX = 9.50
SENIORS_DOWNHILL_TAX = 13.75
SENIORS_ROAD_TAX = 21.50

COSTS_PERCENT = 0.05

number_junior_bikers = int(input())
number_senior_bikers = int(input())
type_of_track = input()

amount_collected = 0

if type_of_track == "trail":
    amount_collected += (number_junior_bikers * JUNIORS_TRAIL_TAX) + (number_senior_bikers * SENIORS_TRAIL_TAX)
elif type_of_track == "cross-country":
    if number_senior_bikers + number_junior_bikers >= 50:
        JUNIORS_CROSS_COUNTRY_TAX -= JUNIORS_CROSS_COUNTRY_TAX * 0.25
        SENIORS_CROSS_COUNTRY_TAX -= SENIORS_CROSS_COUNTRY_TAX * 0.25
        amount_collected += (number_junior_bikers * JUNIORS_CROSS_COUNTRY_TAX) \
                            + (number_senior_bikers * SENIORS_CROSS_COUNTRY_TAX)
    else:
        amount_collected += (number_junior_bikers * JUNIORS_CROSS_COUNTRY_TAX) \
                            + (number_senior_bikers * SENIORS_CROSS_COUNTRY_TAX)
elif type_of_track == "downhill":
    amount_collected += (number_junior_bikers * JUNIORS_DOWNHILL_TAX) + (number_senior_bikers * SENIORS_DOWNHILL_TAX)
elif type_of_track == "road":
    amount_collected += (number_junior_bikers * JUNIORS_ROAD_TAX) + (number_senior_bikers * SENIORS_ROAD_TAX)

money_for_charity = amount_collected - (amount_collected * COSTS_PERCENT)

print(f"{money_for_charity:.2f}")
