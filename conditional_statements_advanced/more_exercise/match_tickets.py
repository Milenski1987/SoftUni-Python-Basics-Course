VIP_TICKET_PRICE = 499.99
NORMAL_TICKET_PRICE = 249.99

TRANSPORT_PERCENT_1_TO_4 = 0.75
TRANSPORT_PERCENT_5_TO_9 = 0.60
TRANSPORT_PERCENT_10_TO_24 = 0.50
TRANSPORT_PERCENT_25_TO_49 = 0.40
TRANSPORT_PERCENT_MORE_THAN_50 = 0.25

budget = float(input())
category = input()
number_of_people_in_group = int(input())

transport_cost = 0
tickets_cost = 0

if 1 <= number_of_people_in_group <= 4:
    transport_cost += budget * TRANSPORT_PERCENT_1_TO_4
elif 5 <= number_of_people_in_group <= 9:
    transport_cost += budget * TRANSPORT_PERCENT_5_TO_9
elif 10 <= number_of_people_in_group <= 24:
    transport_cost += budget * TRANSPORT_PERCENT_10_TO_24
elif 25 <= number_of_people_in_group <= 49:
    transport_cost += budget * TRANSPORT_PERCENT_25_TO_49
elif number_of_people_in_group >= 50:
    transport_cost += budget * TRANSPORT_PERCENT_MORE_THAN_50

if category == "VIP":
    tickets_cost += number_of_people_in_group * VIP_TICKET_PRICE
elif category == "Normal":
    tickets_cost += number_of_people_in_group * NORMAL_TICKET_PRICE

total_cost = tickets_cost + transport_cost
money_diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Yes! You have {money_diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_diff:.2f} leva.")
    