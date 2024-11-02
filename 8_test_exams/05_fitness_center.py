number_of_visitors = int(input())
back_count = chest_count = legs_count = abs_count = shake_count = bar_count = 0

for visitor in range(1, number_of_visitors + 1):
    type_of_activity = input()

    if type_of_activity == "Back":
        back_count += 1
    elif type_of_activity == "Chest":
        chest_count += 1
    elif type_of_activity == "Legs":
        legs_count += 1
    elif type_of_activity == "Abs":
        abs_count += 1
    elif type_of_activity == "Protein shake":
        shake_count += 1
    elif type_of_activity == "Protein bar":
        bar_count += 1

print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{shake_count} - protein shake")
print(f"{bar_count} - protein bar")
print(f"{(((back_count + chest_count + legs_count + abs_count) / number_of_visitors) * 100):.2f}% - work out")
print(f"{(((shake_count + bar_count) / number_of_visitors) * 100):.2f}% - protein")


