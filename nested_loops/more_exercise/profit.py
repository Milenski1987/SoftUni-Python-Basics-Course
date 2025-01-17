coin_1lv = int(input())
coin_2lv = int(input())
buck_5lv = int(input())
amount = int(input())

for coin1 in range(coin_1lv + 1):
    for coin2 in range(coin_2lv + 1):
        for buck in range (buck_5lv + 1):
            if (coin1 * 1) + (coin2 * 2) + (buck * 5) == amount:
                print(f"{coin1} * 1 lv. + {coin2} * 2 lv. + {buck} * 5 lv. = {amount} lv.")