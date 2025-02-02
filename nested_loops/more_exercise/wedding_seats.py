last_sector = input()
rows_in_first_sector = int(input())
seats_in_odd_row = int(input()) + 97

seats_in_even_row = seats_in_odd_row + 2
total_seats = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range (1, rows_in_first_sector + 1):
        if row % 2 != 0:
            for seat in range(97, seats_in_odd_row):
                total_seats += 1
                print(f"{chr(sector)}{row}{chr(seat)}")
        else:
            for seat in range(97, seats_in_even_row):
                total_seats += 1
                print(f"{chr(sector)}{row}{chr(seat)}")

    rows_in_first_sector += 1

print(total_seats)