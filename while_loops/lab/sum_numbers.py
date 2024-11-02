number = int(input())

sum_numbers = 0

while True:
    num = int(input())

    sum_numbers += num

    if sum_numbers >= number:
        print(sum_numbers)
        break
