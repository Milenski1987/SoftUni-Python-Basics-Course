number = input()

a1, a2, a3 = number

for first_digit in range(1, int(a3) + 1):
    for second_digit in range(1, int(a2) + 1):
        for third_digit in range(1, int(a1) + 1):
            result = first_digit * second_digit * third_digit
            print(f"{first_digit} * {second_digit} * {third_digit} = {result};")

