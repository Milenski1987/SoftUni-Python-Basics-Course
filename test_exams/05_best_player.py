best_player = ""
goals_scored = 0
hat_trick = False

while True:
    command = input()

    if command == "END":
        break

    number_of_goals = int(input())
    if number_of_goals > goals_scored:
        best_player = command
        goals_scored = number_of_goals

    if number_of_goals >= 10:
        hat_trick = True
        break
    elif 3 <= number_of_goals <= 10:
        hat_trick = True

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {goals_scored} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals_scored} goals.")


