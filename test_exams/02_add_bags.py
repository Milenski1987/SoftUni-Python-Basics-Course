price_for_luggage_over_20kg = float(input())
kg_of_luggage = float(input())
days_until_travel = int(input())
number_of_luggage = int(input())

bags_tax = 0

if 0 < kg_of_luggage < 10:
    bags_tax = price_for_luggage_over_20kg * 0.20
elif 10 <= kg_of_luggage <= 20:
    bags_tax = price_for_luggage_over_20kg * 0.50
elif kg_of_luggage > 20:
    bags_tax = price_for_luggage_over_20kg

if days_until_travel > 30:
    bags_tax += bags_tax * 0.10
elif 7 <= days_until_travel <= 30:
    bags_tax += bags_tax * 0.15
elif 0 < days_until_travel < 7:
    bags_tax += bags_tax * 0.40

total_sum = number_of_luggage * bags_tax

print(f"The total price of bags is: {total_sum:.2f} lv.")

