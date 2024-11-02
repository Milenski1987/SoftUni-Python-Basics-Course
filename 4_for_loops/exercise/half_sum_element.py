from sys import maxsize

nums = int(input())

max_num = - maxsize
sum_numbers = 0

for _ in range(nums):
    number = int(input())

    if number > max_num:
        max_num = number

    sum_numbers += number

if sum_numbers - max_num == max_num:
    print(f"Yes\nSum = {max_num}")
else:
    print(f"No\nDiff = {abs(max_num - (sum_numbers - max_num))}")
    