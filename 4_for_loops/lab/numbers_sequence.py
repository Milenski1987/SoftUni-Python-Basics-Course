nums = int(input())

max_num = min_num = 0

for num in range(nums):
    number = int(input())

    if num == 0:
        max_num = number
        min_num = number
    else:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")

