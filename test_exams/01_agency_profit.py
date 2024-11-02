company_name = input()
tickets_for_mature = int(input())
tickets_for_kids = int(input())
price_for_mature_ticket = float(input())
tax_for_service = float(input())

price_for_kids_ticket = price_for_mature_ticket * 0.30

total_price = (tickets_for_mature * (price_for_mature_ticket + tax_for_service)) \
              + (tickets_for_kids * (price_for_kids_ticket + tax_for_service))

profit = total_price * 0.20

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")
