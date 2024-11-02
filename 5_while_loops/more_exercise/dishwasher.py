DETERGENT_IN_BOTTLE = 750
DETERGENT_FOR_DISH = 5
DETERGENT_FOR_POT = 15

bottles_of_detergent = int(input())
detergent_in_liters = bottles_of_detergent * DETERGENT_IN_BOTTLE
wash_count = 0
pots_washed = dishes_washed = 0
washed = True
result = None

while True:
    command = input()

    if command == "End":
        break

    more_to_be_washed = int(command)
    wash_count += 1

    if wash_count % 3 == 0:
        detergent_in_liters -= more_to_be_washed * DETERGENT_FOR_POT
        if detergent_in_liters < 0:
            break
        else:
            pots_washed += more_to_be_washed
    else:
        detergent_in_liters -= more_to_be_washed * DETERGENT_FOR_DISH
        if detergent_in_liters < 0:
            break
        else:
            dishes_washed += more_to_be_washed

if detergent_in_liters >= 0:
    print(f"Detergent was enough!\n{dishes_washed} dishes and {pots_washed} pots were washed.")
    print(f"Leftover detergent {detergent_in_liters} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_in_liters)} ml. more necessary!")

