VIDEO_CARD_PRICE = 250
PROCESSOR_PRICE_PERCENT = 0.35
RAM_PERCENT = 0.10
DISCOUNT_PERCENT = 0.15

budget = float(input())
video_card_quantity = int(input())
processors_quantity = int(input())
ram_quantity = int(input())

video_card_total_price = video_card_quantity * VIDEO_CARD_PRICE
processors_total_price = processors_quantity * (video_card_total_price * PROCESSOR_PRICE_PERCENT)
ram_total_price = ram_quantity * (video_card_total_price * RAM_PERCENT)

budget_needed = video_card_total_price + processors_total_price + ram_total_price

if video_card_quantity > processors_quantity:
    budget_needed -= budget_needed * DISCOUNT_PERCENT

if budget >= budget_needed:
    print(f"You have {budget - budget_needed:.2f} leva left!")
else:
    print(f"Not enough money! You need {budget_needed - budget:.2f} leva more!")