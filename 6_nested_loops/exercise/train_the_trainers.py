people_in_jury = int(input())
total_score_for_all_presentations = 0
number_of_presentations = 0
result = ""

while True:

    presentation = input()

    if presentation == "Finish":
        break

    total_score_for_current_presentation = 0
    number_of_presentations += 1

    for _ in range(people_in_jury):
        grade = float(input())

        total_score_for_current_presentation += grade

    result += f"{presentation} - {total_score_for_current_presentation / people_in_jury:.2f}.\n"
    total_score_for_all_presentations += total_score_for_current_presentation

result += (f"Student's final assessment is "
           f"{total_score_for_all_presentations / (people_in_jury * number_of_presentations):.2f}.")
print(result)
