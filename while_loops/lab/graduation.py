name = input()
grade = 1
total_evaluations = 0
fails_count = 0
result = None

while True:
    evaluation = float(input())

    if evaluation >= 4.00:
        total_evaluations += evaluation
        if grade == 12:
            result = f"{name} graduated. Average grade: {total_evaluations / grade:.2f}"
            break
        grade += 1
    else:
        fails_count += 1
        if fails_count > 1:
            result = f"{name} has been excluded at {grade} grade"
            break

print(result)
