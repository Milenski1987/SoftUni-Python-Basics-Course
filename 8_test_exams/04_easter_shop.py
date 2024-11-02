starting_egg_count = int(input())
sold_count = 0

while True:
    command = input()

    if command == "Close":
        print("Store is closed!")
        print(f"{sold_count} eggs sold.")
        break

    eggs_quantity = int(input())
    if command == "Buy":
        if eggs_quantity > starting_egg_count:
            print("Not enough eggs in store!")
            print(f"You can buy only {starting_egg_count}.")
            break
        else:
            starting_egg_count -= eggs_quantity
            sold_count += eggs_quantity
    elif command == "Fill":
        starting_egg_count += eggs_quantity
        