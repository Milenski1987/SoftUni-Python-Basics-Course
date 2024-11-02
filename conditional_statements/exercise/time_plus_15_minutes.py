hour = int(input())
minute = int(input())

new_minute = minute + 15

if new_minute > 59:
    hour += 1
    new_minute -= 60

if hour > 23:
    hour = 0

print(f"{hour}:{new_minute:02d}")


