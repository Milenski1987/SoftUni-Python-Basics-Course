time_for_shooting = int(input())
number_of_scenes = int(input())
duration_of_scene = int(input())

preparing = time_for_shooting * 0.15

time_needed = (number_of_scenes * duration_of_scene) + preparing
time_diff = abs(time_needed - time_for_shooting)

if time_for_shooting >= time_needed:
    print(f"You managed to finish the movie on time! You have {round(time_diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(time_diff)} minutes.")

