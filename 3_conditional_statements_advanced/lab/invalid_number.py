number = int(input())
is_valid = False

if 100 <= number <= 200 or number == 0:
    is_valid = True

if not is_valid:
    print("invalid")

