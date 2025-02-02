from math import floor

number_of_balls = int(input())
score = 0
red_count = orange_count = yellow_count = white_count = black_count = others_count = 0

for ball in range(number_of_balls):
    color = input()

    if color == "red":
        score += 5
        red_count +=1
    elif color == "orange":
        score += 10
        orange_count += 1
    elif color == "yellow":
        score += 15
        yellow_count += 1
    elif color == "white":
        score += 20
        white_count += 1
    elif color == "black":
        score = floor(score / 2)
        black_count += 1
    else:
        score += 0
        others_count += 1

print(f"Total points: {score}")
print(f"Red balls: {red_count}")
print(f"Orange balls: {orange_count}")
print(f"Yellow balls: {yellow_count}")
print(f"White balls: {white_count}")
print(f"Other colors picked: {others_count}")
print(f"Divides from black balls: {black_count}")

