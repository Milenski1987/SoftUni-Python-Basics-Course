PREMIERE = 12
NORMAL = 7.50
DISCOUNT = 5

type_of_projection = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns

if type_of_projection == "Premiere":
    income = cinema_capacity * PREMIERE
elif type_of_projection == "Normal":
    income = cinema_capacity * NORMAL
elif type_of_projection == "Discount":
    income = cinema_capacity * DISCOUNT

print(f"{income:.2f} leva")
