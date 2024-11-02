from math import floor

n = int(input())

rows = floor((n + 1) / 2)

for row in range(1, rows + 1):
    if row == 1:
        if n % 2 == 0:
            y = row * 2
            i = int((n - y) / 2)
            print(i * "-" + y * "*" + i * "-")
        else:
            y = row
            i = int((n - y) / 2)
            print(i * "-" + y * "*" + i * "-")
    else:
        if n % 2 == 0:
            y = int ((2 * row) / 2)
            i = int((n - (2 * row)) / 2)
            print(i * "-" + 2 * row * "*" + i * "-")
        else:
            y = 2 * row - 1
            i = int((n - y) / 2)
            print(i * "-" + y * "*" + i * "-")

rows_down = floor(n / 2)

for row_down in range(1, rows_down + 1):
    j = n - 2
    print("|" + (j * "*") + "|")
