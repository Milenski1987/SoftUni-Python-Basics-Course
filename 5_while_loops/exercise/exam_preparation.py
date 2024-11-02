number_of_poor_grades_allowed = int(input())

poor_grades_count = 0
total_score = 0
number_of_tasks = 0
last_task = ""

while True:
    task_name = input()

    if task_name == "Enough":
        print(f"Average score: {total_score / number_of_tasks:.2f}")
        print(f"Number of problems: {number_of_tasks}")
        print(f"Last problem: {last_task}")
        break

    last_task = task_name
    number_of_tasks += 1
    grade = int(input())

    if grade <= 4:
        poor_grades_count += 1
        if poor_grades_count == number_of_poor_grades_allowed:
            print(f"You need a break, {poor_grades_count} poor grades.")
            break
    total_score += grade
