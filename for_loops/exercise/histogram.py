n = int(input())

p_under_200 = p_200_399 = p_400_599 = p_600_799 = p_over_800 = 0

for _ in range(n):
    number = int(input())

    if number < 200:
        p_under_200 += 1
    elif number < 400:
        p_200_399 += 1
    elif number < 600:
        p_400_599 += 1
    elif number < 800:
        p_600_799 += 1
    elif number <= 1000:
        p_over_800 += 1

print(f"{(p_under_200 / n * 100):.2f}%")
print(f"{(p_200_399 / n * 100):.2f}%")
print(f"{(p_400_599 / n * 100):.2f}%")
print(f"{(p_600_799 / n * 100):.2f}%")
print(f"{(p_over_800 / n * 100):.2f}%")
