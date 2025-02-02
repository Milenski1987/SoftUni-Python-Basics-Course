from math import floor

LAST_EPISODE_ADDITIONAL_TIME = 10

name_of_tv_series = input()
seasons = int(input())
episodes = int(input())
duration_of_episode = float(input())
advertising = duration_of_episode * 0.20

duration_of_season = (episodes * duration_of_episode) + (episodes * advertising) + LAST_EPISODE_ADDITIONAL_TIME

total_time_needed = duration_of_season * seasons

print(f"Total time needed to watch the {name_of_tv_series} series is {floor(total_time_needed)} minutes.")

