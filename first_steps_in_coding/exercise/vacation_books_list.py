pages_in_current_book = int(input())
pages_read_per_hour = int(input())
days_to_read_book = int(input())

total_hours = pages_in_current_book // pages_read_per_hour
hours_per_day = total_hours // days_to_read_book

print(hours_per_day)
