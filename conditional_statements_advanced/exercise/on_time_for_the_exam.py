hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrive = int(input())
minute_of_arrive = int(input())

time_of_exam_in_minutes = (hour_of_exam * 60) + minute_of_exam
time_of_arrive_in_minute = (hour_of_arrive * 60) + minute_of_arrive

time_diff = time_of_exam_in_minutes - time_of_arrive_in_minute

if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")

hours = abs(time_diff) // 60
minutes = abs(time_diff) % 60

result = ""

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_diff > 0:
    result += " before the start"
elif time_diff < 0:
    result += " after the start"

print(result)
