budget_for_actors = float(input())
budget_left = budget_for_actors

while True:
    command = input()
    actor_salary = 0

    if command == "ACTION":
        break

    if len(command) <= 15:
        actor_salary = float(input())
    else:
        actor_salary = budget_left * 0.20

    budget_left -= actor_salary
    if budget_left < 0:
        break

if budget_left >= 0:
    print(f"We are left with {budget_left:.2f} leva.")
else:
    print(f"We need {abs(budget_left):.2f} leva for our actors.")
    