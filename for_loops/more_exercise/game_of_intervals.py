number_of_moves = int(input())

num_0_9_count = num_10_19_count = num_20_29_count = num_30_39_count = num_40_50_count = invalid_num = 0
score = 0

for _ in range(number_of_moves):
    number = int(input())

    if number < 0 or number > 50:
        invalid_num += 1
        score -= score / 2
    elif number <= 9:
        num_0_9_count += 1
        score += number * 0.20
    elif number <= 19:
        num_10_19_count += 1
        score += number * 0.30
    elif number <= 29:
        num_20_29_count += 1
        score += number * 0.40
    elif number <= 39:
        num_30_39_count += 1
        score += 50
    elif number <= 50:
        num_40_50_count += 1
        score += 100

percent_0_9 = num_0_9_count / number_of_moves * 100
percent_10_19 = num_10_19_count / number_of_moves * 100
percent_20_29 = num_20_29_count / number_of_moves * 100
percent_30_39 = num_30_39_count / number_of_moves * 100
percent_40_50 = num_40_50_count / number_of_moves * 100
percent_invalid = invalid_num / number_of_moves * 100

print(f"{score:.2f}")
print(f"From 0 to 9: {percent_0_9:.2f}%")
print(f"From 10 to 19: {percent_10_19:.2f}%")
print(f"From 20 to 29: {percent_20_29:.2f}%")
print(f"From 30 to 39: {percent_30_39:.2f}%")
print(f"From 40 to 50: {percent_40_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")

