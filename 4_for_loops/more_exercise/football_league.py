stadium_capacity = int(input())
number_of_fans = int(input())

sector_a_count = sector_b_count = sector_v_count = sector_g_count = 0

for _ in range(number_of_fans):
    sector = input()

    if sector == "A":
        sector_a_count += 1
    if sector == "B":
        sector_b_count += 1
    if sector == "V":
        sector_v_count += 1
    if sector == "G":
        sector_g_count += 1

sector_a_percent = sector_a_count / number_of_fans * 100
sector_b_percent = sector_b_count / number_of_fans * 100
sector_v_percent = sector_v_count / number_of_fans * 100
sector_g_percent = sector_g_count / number_of_fans * 100
total_fans_percent = number_of_fans / stadium_capacity * 100

print(f"{sector_a_percent:.2f}%")
print(f"{sector_b_percent:.2f}%")
print(f"{sector_v_percent:.2f}%")
print(f"{sector_g_percent:.2f}%")
print(f"{total_fans_percent:.2f}%")
