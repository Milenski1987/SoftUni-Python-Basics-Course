actor_name = input()
points_from_academy = float(input())
number_of_judges = int(input())
actor_score = points_from_academy

for judge in range(number_of_judges):
    name_of_the_judge = input()
    points_from_judge = float(input())

    actor_score += len(name_of_the_judge) * points_from_judge / 2

    if actor_score > 1250.5:
        break

if actor_score >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_score:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - actor_score):.1f} more!")

    

