number_of_locations = int(input())

for _ in range(number_of_locations):
    expected_average_yield_per_day = float(input())
    number_of_days_for_current_location = int(input())

    total_gold_mined = 0

    for __ in range(number_of_days_for_current_location):
        gold_mined_for_current_day = float(input())

        total_gold_mined += gold_mined_for_current_day

    average_gold_per_location = total_gold_mined / number_of_days_for_current_location

    yield_diff = abs(expected_average_yield_per_day - average_gold_per_location)

    if average_gold_per_location >= expected_average_yield_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_location:.2f}.")
    else:
        print(f"You need {yield_diff:.2f} gold.")

