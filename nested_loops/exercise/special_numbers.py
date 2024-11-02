# number = int(input())
#
# for num1 in range(1, 10):
#     if number % num1 == 0:
#         for num2 in range(1, 10):
#             if number % num2 == 0:
#                 for num3 in range(1, 10):
#                     if number % num3 == 0:
#                         for num4 in range(1, 10):
#                             if number % num4 == 0:
#                                 print(f"{num1}{num2}{num3}{num4}", end=" ")

number = int(input())

for num in range(1111, 9999 + 1):
    special_number = True
    for digit in (str(num)):
        if 0 < int(digit) < 10:
            if number % int(digit) != 0:
                special_number = False

    if special_number:
        print(num, end=" ")
