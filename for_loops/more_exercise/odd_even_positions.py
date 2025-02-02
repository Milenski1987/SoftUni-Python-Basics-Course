from sys import maxsize

n = int(input())

odd_sum = even_sum = 0
min_odd_num = min_even_num = maxsize
max_odd_num = max_even_num = -maxsize


for position in range(1, n + 1):
    number = float(input())

    if position % 2 != 0:
        odd_sum += number

        if number > max_odd_num:
            max_odd_num = number
        if number < min_odd_num:
            min_odd_num = number

    else:
        even_sum += number

        if number > max_even_num:
            max_even_num = number
        if number < min_even_num:
            min_even_num = number

print(f"OddSum={odd_sum:.2f},")
if min_odd_num == maxsize and max_odd_num == -maxsize:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
else:
    print(f"OddMin={min_odd_num:.2f},")
    print(f"OddMax={max_odd_num:.2f},")
print(f"EvenSum={even_sum:.2f},")
if min_even_num == maxsize and max_even_num == -maxsize:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenMin={min_even_num:.2f},")
    print(f"EvenMax={max_even_num:.2f}")










