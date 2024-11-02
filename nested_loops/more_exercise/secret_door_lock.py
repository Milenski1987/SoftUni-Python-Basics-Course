hundreds_border = int(input())
tenths_border = int(input())
units_border = int(input())

for num1 in range(1, hundreds_border + 1):
    if num1 % 2 == 0:
        for num2 in range(1, tenths_border + 1):
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                for num3 in range(1, units_border + 1):
                    if num3 % 2 == 0:
                        print(f"{num1} {num2} {num3}")

