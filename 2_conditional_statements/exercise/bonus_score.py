starting_points = int(input())
points = 0

if starting_points <= 100:
    points += 5
elif starting_points <= 1000:
    points += starting_points * 0.20
elif starting_points > 1000:
    points += starting_points * 0.10

if starting_points % 2 == 0:
    points += 1

if starting_points % 10 == 5:
    points += 2

print(points)
print(points + starting_points)
