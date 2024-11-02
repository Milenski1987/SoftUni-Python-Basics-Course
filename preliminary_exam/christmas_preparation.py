WRAPPING_PAPER_PRICE = 5.80
CLOTH_PRICE = 7.20
GLUE_PRICE = 1.20

wrapping_paper_quantity = int(input())
cloth_quantity = int(input())
glue_amount = float(input())
percent_discount = int(input())

money_needed = (WRAPPING_PAPER_PRICE * wrapping_paper_quantity) + (CLOTH_PRICE * cloth_quantity) + (GLUE_PRICE * glue_amount)
discount = money_needed * (percent_discount / 100)

total_money_needed = money_needed - discount

print(f"{total_money_needed:.3f}")
