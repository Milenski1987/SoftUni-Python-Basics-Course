trunk_capacity = float(input())


suitcases_count = 0
result = ""

while trunk_capacity > 0:
    command = input()

    if command == "End":
        result += "Congratulations! All suitcases are loaded!\n"
        break

    suitcase_volume = float(command)
    suitcases_count += 1

    if suitcases_count % 3 == 0:
        suitcase_volume += suitcase_volume * 0.10

    trunk_capacity -= suitcase_volume

else:
    result += "No more space!\n"
    suitcases_count -= 1

result += f"Statistic: {suitcases_count} suitcases loaded."

print(result)
