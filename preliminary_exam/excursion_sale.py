SEA_PRICE = 680
MOUNTAIN_PRICE = 499

number_of_sea_trips = int(input())
number_of_mountain_trips = int(input())

profit = 0

while True:
    package = input()

    if package == "Stop":
        break

    elif package == "sea":
        if number_of_sea_trips < 1:
            continue
        else:
            profit += SEA_PRICE
            number_of_sea_trips -= 1

    elif package == "mountain":
        if number_of_mountain_trips < 1:
            continue
        else:
            profit += MOUNTAIN_PRICE
            number_of_mountain_trips -= 1

    if number_of_mountain_trips < 1 and number_of_sea_trips < 1:
        print("Good job! Everything is sold.")
        break


print(f"Profit: {profit} leva.")
