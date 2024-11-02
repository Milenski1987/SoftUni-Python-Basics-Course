money_needed = float(input())
available_money = float(input())

days_count = 0
spending_days_count = 0
result = ""

while True:
    action = input()
    days_count += 1
    amount = float(input())

    if action == "spend":
        available_money -= amount
        if available_money < 0:
            available_money = 0
        spending_days_count += 1
        if spending_days_count == 5:
            result = f"You can't save the money.\n{days_count}"
            break

    elif action == "save":
        available_money += amount
        spending_days_count = 0
        if available_money >= money_needed:
            result = f"You saved the money for {days_count} days."
            break

print(result)
