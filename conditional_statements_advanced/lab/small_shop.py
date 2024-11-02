product = input()
city = input()
quantity = float(input())

price_of_products = 0

if city == "Sofia":
    if product == "coffee":
        price_of_products = 0.50 * quantity
    elif product == "water":
        price_of_products = 0.80 * quantity
    elif product == "beer":
        price_of_products = 1.20 * quantity
    elif product == "sweets":
        price_of_products = 1.45 * quantity
    elif product == "peanuts":
        price_of_products = 1.60 * quantity
if city == "Plovdiv":
    if product == "coffee":
        price_of_products = 0.40 * quantity
    elif product == "water":
        price_of_products = 0.70 * quantity
    elif product == "beer":
        price_of_products = 1.15 * quantity
    elif product == "sweets":
        price_of_products = 1.30 * quantity
    elif product == "peanuts":
        price_of_products = 1.50 * quantity
if city == "Varna":
    if product == "coffee":
        price_of_products = 0.45 * quantity
    elif product == "water":
        price_of_products = 0.70 * quantity
    elif product == "beer":
        price_of_products = 1.10 * quantity
    elif product == "sweets":
        price_of_products = 1.35 * quantity
    elif product == "peanuts":
        price_of_products = 1.55 * quantity

print(price_of_products)

        
