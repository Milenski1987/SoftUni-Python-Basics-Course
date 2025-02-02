degrees = float(input())

if 5.00 <= degrees < 12.0:
    print("Cold")
elif 12.00 <= degrees < 15.0:
    print("Cool")
elif 15.00 <= degrees <= 20.00:
    print("Mild")
elif 20.0 < degrees < 26.0:
    print("Warm")
elif 26.00 <= degrees <= 35.00:
    print("Hot")
else:
    print("unknown")
