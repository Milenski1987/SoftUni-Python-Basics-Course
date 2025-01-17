from math import ceil

LUNCH_TIME = 1 / 8
REST_TIME = 1 / 4

tv_series_name = input()
episode_length = int(input())
rest_length = int(input())

rest_time_left = rest_length - ((rest_length * LUNCH_TIME) + (rest_length * REST_TIME))

if episode_length <= rest_time_left:
    print(f"You have enough time to watch {tv_series_name} and "
          f"left with {ceil(rest_time_left - episode_length)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_series_name}, "
          f"you need {ceil(episode_length - rest_time_left)} more minutes.")
