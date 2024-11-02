number_1 = int(input())
number_2 = int(input())

#
# for number in range(number_1, number_2 + 1):
#     even_sum = odd_sum = 0
#     for idx, digits in enumerate(str(number)):
#         if idx % 2 == 0:
#             even_sum += int(digits)
#         else:
#             odd_sum += int(digits)
#
#     if even_sum == odd_sum:
#         print(number, end=" ")

for number in range(number_1, number_2 + 1):

    a1, a2, a3, a4, a5, a6 = str(number)

    if int(a1) + int(a3) + int(a5) == int(a2) + int(a4) + int(a6):
        print(number, end=" ")


