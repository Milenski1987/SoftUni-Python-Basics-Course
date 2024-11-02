number_of_pc = int(input())

total_sales_made = 0
total_rating = 0

for _ in range(number_of_pc):
    rating = input()
    total_rating += int(rating[-1])

    possible_sales_percent = 0

    if int(rating[-1]) == 2:
        possible_sales_percent += 0
    elif int(rating[-1]) == 3:
        possible_sales_percent += 0.50
    elif int(rating[-1]) == 4:
        possible_sales_percent += 0.70
    elif int(rating[-1]) == 5:
        possible_sales_percent += 0.85
    elif int(rating[-1]) == 6:
        possible_sales_percent += 1

    possible_sales = int(rating[:2])

    sales_made = possible_sales * possible_sales_percent
    total_sales_made += sales_made

average_rating = total_rating / number_of_pc

print(f"{total_sales_made:.2f}\n{average_rating:.2f}")
