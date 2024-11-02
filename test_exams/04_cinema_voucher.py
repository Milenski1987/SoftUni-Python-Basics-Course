voucher_value = int(input())
tickets_count = 0
other_purchases_count = 0
money_spent = 0

while True:
    purchase = input()

    if purchase == "End":
        break

    if len(purchase) > 8:
        money_spent += ord(purchase[0]) + ord(purchase[1])
        if money_spent > voucher_value:
            break
        else:
            tickets_count += 1
    else:
        money_spent += ord(purchase[0])
        if money_spent > voucher_value:
            break
        else:
            other_purchases_count += 1

    if money_spent > voucher_value:
        break

print(f"{tickets_count}")
print(f"{other_purchases_count}")


