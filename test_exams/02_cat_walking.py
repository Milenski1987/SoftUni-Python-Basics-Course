CAL_PER_MIN = 5
THRESHOLD_PERCENT = 0.50


minutes_per_walking = int(input())
number_of_walking = int(input())
cal_taken = int(input())
result = ""

walking_goal = cal_taken * THRESHOLD_PERCENT

cal_burned = (number_of_walking * minutes_per_walking) * CAL_PER_MIN

result += (f"Yes, the walk for your cat is enough. "
           f"Burned calories per day: {cal_burned}.") \
    if cal_burned >= walking_goal else f"No, the walk for your cat is not enough. Burned calories per day: {cal_burned}."

print(result)
