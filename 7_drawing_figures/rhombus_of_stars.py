n = int(input())

for row in range(1, n):
    print((n - row) * " " + "*" + (row - 1) * " *")

for row1 in range(n, 0, - 1):
    print((n - row1) * " " + "*" + (row1 - 1) * " *")
