bill_change = float(input())

bill_change_in_st = int(bill_change * 100)
coins_count = 0

while bill_change_in_st > 0:

    if bill_change_in_st >= 200:
        bill_change_in_st -= 200

    elif bill_change_in_st >= 100:
        bill_change_in_st -= 100

    elif bill_change_in_st >= 50:
        bill_change_in_st -= 50

    elif bill_change_in_st >= 20:
        bill_change_in_st -= 20

    elif bill_change_in_st >= 10:
        bill_change_in_st -= 10

    elif bill_change_in_st >= 5:
        bill_change_in_st -= 5

    elif bill_change_in_st >= 2:
        bill_change_in_st -= 2

    elif bill_change_in_st >= 1:
        bill_change_in_st -= 1

    coins_count += 1

print(coins_count)

