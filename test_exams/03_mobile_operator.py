term_of_contract = input()
type_of_contract = input()
additional_mobile_internet = input()
months_to_pay = int(input())

monthly_tax = 0

if term_of_contract == "one":
    if type_of_contract == "Small":
        monthly_tax += 9.98
    elif type_of_contract == "Middle":
        monthly_tax += 18.99
    elif type_of_contract == "Large":
        monthly_tax += 25.98
    elif type_of_contract == "ExtraLarge":
        monthly_tax += 35.99
elif term_of_contract == "two":
    if type_of_contract == "Small":
        monthly_tax += 8.58
    elif type_of_contract == "Middle":
        monthly_tax += 17.09
    elif type_of_contract == "Large":
        monthly_tax += 23.59
    elif type_of_contract == "ExtraLarge":
        monthly_tax += 31.79

if additional_mobile_internet == "yes":
    if monthly_tax <= 10:
        monthly_tax += 5.50
    elif monthly_tax <= 30:
        monthly_tax += 4.35
    else:
        monthly_tax += 3.85

total_price = months_to_pay * monthly_tax

if term_of_contract == "two":
    total_price -= total_price * 0.0375

print(f"{total_price:.2f} lv.")



