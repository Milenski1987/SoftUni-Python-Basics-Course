groups = int(input())

musala_count = montblanc_count = kilimanjaro_count = k2_count = everest_count = 0
total_people = 0

for _ in range(groups):
    people = int(input())

    if people <= 5:
        musala_count += people
    elif people <= 12:
        montblanc_count += people
    elif people <= 25:
        kilimanjaro_count += people
    elif people <= 40:
        k2_count += people
    elif people > 40:
        everest_count += people

total_people = musala_count + montblanc_count + kilimanjaro_count + k2_count + everest_count

musala_percent = musala_count / total_people * 100
montblanc_percent = montblanc_count / total_people * 100
kilimanjaro_percent = kilimanjaro_count / total_people * 100
k2_percent = k2_count / total_people * 100
everest_percent = everest_count / total_people * 100

print(f"{musala_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
