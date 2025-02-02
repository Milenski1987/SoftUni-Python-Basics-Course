price_of_mackerel = float(input())
price_of_sprinkle = float(input())
quantity_bonito = float(input())
quantity_scad = float(input())
quantity_shells = int(input())

price_of_bonito = price_of_mackerel + (price_of_mackerel * 0.60)
price_of_scad = price_of_sprinkle + (price_of_sprinkle * 0.80)
price_of_shells = 7.50

total_sum = (quantity_bonito * price_of_bonito) + (quantity_scad * price_of_scad) + \
            (quantity_shells * price_of_shells)

print(f"{total_sum:.2f}")