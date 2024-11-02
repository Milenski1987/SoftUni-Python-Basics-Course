expected_sum = int(input())

collected_sum = 0
cash_sum = card_sum = 0
cash_count = card_count = 0
payment_count = 1

while collected_sum < expected_sum:
    command = input()

    if command == "End":
        print("Failed to collect required money for charity.")
        break

    price_of_item = int(command)

    if payment_count % 2 != 0:
        if price_of_item > 100:
            print("Error in transaction!")
        else:
            cash_sum += price_of_item
            cash_count += 1
            collected_sum += price_of_item
            print("Product sold!")
    else:
        if price_of_item < 10:
            print("Error in transaction!")
        else:
            card_sum += price_of_item
            card_count += 1
            collected_sum += price_of_item
            print("Product sold!")

    payment_count += 1

else:
    print(f"Average CS: {cash_sum / cash_count:.2f}\nAverage CC: {card_sum / card_count:.2f}")
