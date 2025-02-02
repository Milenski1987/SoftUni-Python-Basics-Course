WORKING_DAY_PLAY_TIME = 63
RESTING_DAY_PLAY_TIME = 127
TOM_PLAYING_TIME_NORM = 30000

rest_days = int(input())
work_days = 365 - rest_days

total_playing_time = rest_days * RESTING_DAY_PLAY_TIME + work_days * WORKING_DAY_PLAY_TIME
play_time_dif = abs(TOM_PLAYING_TIME_NORM - total_playing_time)
play_hours_dif = play_time_dif // 60
play_min_dif = play_time_dif % 60


if TOM_PLAYING_TIME_NORM < total_playing_time:
    print("Tom will run away")
    print(f"{play_hours_dif} hours and {play_min_dif} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{play_hours_dif} hours and {play_min_dif} minutes less for play")


