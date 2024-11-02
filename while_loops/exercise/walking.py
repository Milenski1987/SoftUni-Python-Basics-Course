STEPS_GOAL = 10000

total_steps = 0

while total_steps < STEPS_GOAL:
    command = input()

    if command == "Going home":
        steps_going_home = int(input())
        total_steps += steps_going_home
        if total_steps < STEPS_GOAL:
            print(f"{STEPS_GOAL - total_steps} more steps to reach goal.")
            break
        continue

    steps_count = int(command)

    total_steps += steps_count

else:
    print(f"Goal reached! Good job!\n{total_steps - STEPS_GOAL} steps over the goal!")

