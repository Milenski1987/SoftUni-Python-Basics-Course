number_of_groups = int(input())

musala_count = monblan_count = kilimanjaro_count = k2_count = everest_count = total_people = 0

for _ in range(number_of_groups):
    number_of_people = int(input())

    if number_of_people <= 5:
        musala_count += number_of_people
        total_people += number_of_people
    elif number_of_people <= 12:
        monblan_count += number_of_people
        total_people += number_of_people
    elif number_of_people <= 25:
        kilimanjaro_count += number_of_people
        total_people += number_of_people
    elif number_of_people <= 40:
        k2_count += number_of_people
        total_people += number_of_people
    elif number_of_people > 40:
        everest_count += number_of_people
        total_people += number_of_people

musala_percent = musala_count / total_people * 100
monblan_percent = monblan_count / total_people * 100
kilimanjaro_percent = kilimanjaro_count / total_people * 100
k2_percent = k2_count / total_people * 100
everest_percent = everest_count / total_people * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
