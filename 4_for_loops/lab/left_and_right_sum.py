nums = int(input())

left_numbers_sum = right_numbers_sum = 0

for left_num in range(nums):
    left_number = int(input())
    left_numbers_sum += left_number

for right_num in range(nums):
    right_number = int(input())
    right_numbers_sum += right_number

diff = abs(left_numbers_sum- right_numbers_sum
           )
if left_numbers_sum == right_numbers_sum:
    print(f"Yes, sum = {left_numbers_sum}")
else:
    print(f"No, diff = {diff}")

