first_num_threshold = int(input())
second_num_threshold = int(input())
third_num_threshold = int(input())

for num1 in range(1,first_num_threshold + 1):
    if num1 % 2 == 0:
        for num2 in range(1, second_num_threshold + 1):
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                for num3 in range(1, third_num_threshold + 1):
                    if num3 % 2 == 0:
                        print(f"{num1} {num2} {num3}")
