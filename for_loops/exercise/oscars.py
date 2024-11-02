NOMINEE_SCORE = 1250.5

actor_name = input()
academy_points = float(input())
number_of_judges = int(input())

actor_score = academy_points
result = None

for _ in range(number_of_judges):
    judge_name = input()
    judge_points = float(input())

    actor_score += (len(judge_name) * judge_points) / 2

    if actor_score >= NOMINEE_SCORE:
        result = f"Congratulations, {actor_name} got a nominee for leading role with {actor_score:.1f}!"
        break

else:
    result = f"Sorry, {actor_name} you need {NOMINEE_SCORE - actor_score:.1f} more!"

print(result)
