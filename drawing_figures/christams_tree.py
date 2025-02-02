n = int(input())


print((n + 1) * " " + "|")
for row in range(1, n):
    print((n - row) * " " + row * "*" + " | " + row * "*")

