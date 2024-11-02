balance = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break

    income = float(command)
    if income < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {income:.2f}")

    balance += income

print(f"Total: {balance:.2f}")
