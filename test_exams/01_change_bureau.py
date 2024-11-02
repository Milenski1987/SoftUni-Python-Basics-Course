BITCOIN_TO_LV = 1168
CHINA_IAN_TO_USD = 0.15
USD_TO_LV = 1.76
EURO_TO_LV = 1.95

amount_bitcoins = int(input())
amount_china_ian = float(input())
commission = float(input())

china_ian_to_lv = CHINA_IAN_TO_USD * USD_TO_LV

bitcoin_to_euro = (amount_bitcoins * BITCOIN_TO_LV) / EURO_TO_LV
china_ian_to_euro = (amount_china_ian * china_ian_to_lv) / EURO_TO_LV

total_euro = (bitcoin_to_euro + china_ian_to_euro) - ((bitcoin_to_euro + china_ian_to_euro) * (commission / 100))

print(f"{total_euro:.2f}")
