start_of_first_pair = int(input())
start_of_second_pair = int(input())
first_pair_range_diff = int(input())
second_pair_range_diff = int(input())

final_of_first_pair = start_of_first_pair + first_pair_range_diff
final_of_second_pair = start_of_second_pair + second_pair_range_diff



for first_pair in range(start_of_first_pair, final_of_first_pair + 1):
    for second_pair in range(start_of_second_pair, final_of_second_pair + 1):
        first_pair_non_prime = False
        second_pair_non_prime = False

        for num1 in range(2, int(first_pair ** 0.5) + 1):
            if first_pair % num1 == 0:
                first_pair_non_prime = True
            for num2 in range(2, int(second_pair ** 0.5) + 1):
                if second_pair % num2 == 0:
                    second_pair_non_prime = True

        if not first_pair_non_prime and not second_pair_non_prime:
            print(f"{first_pair}{second_pair}")



