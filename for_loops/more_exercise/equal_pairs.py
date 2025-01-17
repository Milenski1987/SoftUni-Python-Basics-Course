n = int(input())

start_sum = 0
max_diff = 0
diff = 0
for i in range(n):
    num1 = int(input())
    num2 = int(input())

    nums_sum = num1 + num2

    if i == 0:
        start_sum = nums_sum

    if nums_sum != start_sum:
        diff = abs(nums_sum - start_sum)
        start_sum = nums_sum

    if diff > max_diff:
        max_diff = diff

if diff == 0:
    print(f"Yes, value={start_sum}")
else:
    print(f"No, maxdiff={max_diff}")

        