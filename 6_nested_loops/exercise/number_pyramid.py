n = int(input())

current_number = 1
bigger_than_n = False

for row in range(1, n + 1):
    for col in range (1, row + 1):
        print(current_number, end=" ")
        current_number += 1

        if current_number > n:
            bigger_than_n = True
            break
    if bigger_than_n:
        break
    print()
