from math import ceil

FLOUR_PACK_WEIGHT = 750
SUGAR_PACK_WEIGHT = 950

number_of_coz = int(input())
max_sugar_used = 0
max_flour_used = 0
sugar_used = 0
flour_used = 0

for coz in range(number_of_coz):
    sugar_spend = int(input())
    flour_spend = int(input())

    sugar_used += sugar_spend
    flour_used += flour_spend

    if sugar_spend > max_sugar_used:
        max_sugar_used = sugar_spend
    if flour_spend > max_flour_used:
        max_flour_used = flour_spend

sugar_packs = ceil(sugar_used / SUGAR_PACK_WEIGHT)
flour_packs = ceil(flour_used / FLOUR_PACK_WEIGHT)

print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")


