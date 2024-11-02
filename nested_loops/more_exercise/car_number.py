start_num = int(input())
end_num = int(input())

for num1 in range(start_num, end_num + 1):
    for num2 in range(start_num, end_num + 1):
        for num3 in range(start_num, end_num + 1):
            for num4 in range(start_num, end_num + 1):
                if (num1 % 2 == 0 and num4 % 2 != 0) or (num1 % 2 != 0 and num4 % 2 == 0):
                    if num1 > num4 and (num2 + num3) % 2 == 0:
                        print(f"{num1}{num2}{num3}{num4}", end=" ")


