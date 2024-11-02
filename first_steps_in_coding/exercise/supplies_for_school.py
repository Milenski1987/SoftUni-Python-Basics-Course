PRICE_PENS = 5.80
PRICE_MARKERS = 7.20
PRICE_DETERGENT = 1.20

number_of_pens = int(input())
number_of_markers = int(input())
amount_detergent = int(input())
discount_percent = int(input()) / 100

total_price_for_pens = number_of_pens * PRICE_PENS
total_price_for_markers = number_of_markers * PRICE_MARKERS
total_price_for_detergent = amount_detergent * PRICE_DETERGENT

total_sum = total_price_for_detergent + total_price_for_markers + total_price_for_pens
final_sum = total_sum - (total_sum * discount_percent)

print(final_sum)
