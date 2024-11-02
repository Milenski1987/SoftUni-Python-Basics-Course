first_player_time = int(input())
second_player_time = int(input())
third_player_time = int(input())

total_time_in_seconds = first_player_time + second_player_time + third_player_time

time_in_minutes = total_time_in_seconds // 60
time_in_seconds = total_time_in_seconds % 60
if time_in_seconds < 10:
    print(f"{time_in_minutes}:0{time_in_seconds}")
else:
    print(f"{time_in_minutes}:{time_in_seconds}")
