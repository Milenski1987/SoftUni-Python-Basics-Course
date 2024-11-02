WATER_TAX = 20
INTERNET_TAX = 15
OTHER_TAXES_PERCENT = 0.20

months = int(input())
electricity_total_payment = internet_total_payment = water_total_payment = other_total_payment = 0

for _ in range(months):
    electricity_tax = float(input())
    other_total_payment += (electricity_tax + INTERNET_TAX
                            + WATER_TAX) + ((electricity_tax + INTERNET_TAX + WATER_TAX) * OTHER_TAXES_PERCENT)
    electricity_total_payment += electricity_tax

internet_total_payment = months * INTERNET_TAX
water_total_payment = months * WATER_TAX

average_payment = (electricity_total_payment + internet_total_payment
                   + water_total_payment + other_total_payment) / months

print(f"Electricity: {electricity_total_payment:.2f} lv")
print(f"Water: {water_total_payment:.2f} lv")
print(f"Internet: {internet_total_payment:.2f} lv")
print(f"Other: {other_total_payment:.2f} lv")
print(f"Average: {average_payment:.2f} lv")
