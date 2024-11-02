minutes_on_spot = int(input())
seconds_on_spot = int(input())
length_of_chute = float(input())
seconds_per_100m = int(input())

acceleration = (length_of_chute / 120) * 2.5
total_spot_time_in_seconds = minutes_on_spot * 60 + seconds_on_spot

total_time_achieved = ((length_of_chute / 100) * seconds_per_100m) - acceleration

if total_time_achieved <= total_spot_time_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time_achieved:.3f}.")
else:
    print(f"No, Marin failed! He was {(total_time_achieved - total_spot_time_in_seconds):.3f} second slower.")
