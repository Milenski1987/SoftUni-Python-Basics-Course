number_of_mens = int(input())
number_of_women = int(input())
number_of_tables = int(input())

table_count = 0


for men in range(1, number_of_mens + 1):
    for woman in range(1, number_of_women + 1):
        print(f"({men} <-> {woman})", end=" ")
        table_count += 1

        if table_count == number_of_tables:
            break
    if table_count == number_of_tables:
        break
