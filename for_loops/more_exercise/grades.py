number_of_students = int(input())

poor_count = middle_count = good_count = very_good_count = 0
grades_sum = 0

for _ in range(number_of_students):
    grade = float(input())

    if 2.00 <= grade <= 2.99:
        poor_count += 1
        grades_sum += grade
    elif 3.00 <= grade <= 3.99:
        middle_count += 1
        grades_sum += grade
    elif 4.00 <= grade <= 4.99:
        good_count += 1
        grades_sum += grade
    elif 5.00 <= grade:
        very_good_count += 1
        grades_sum += grade

poor_percent = poor_count / number_of_students * 100
middle_percent = middle_count / number_of_students * 100
good_percent = good_count / number_of_students * 100
very_good_percent = very_good_count / number_of_students * 100
average_grade = grades_sum / number_of_students

print(f"Top students: {very_good_percent:.2f}%")
print(f"Between 4.00 and 4.99: {good_percent:.2f}%")
print(f"Between 3.00 and 3.99: {middle_percent:.2f}%")
print(f"Fail: {poor_percent:.2f}%")
print(f"Average: {average_grade:.2f}")
