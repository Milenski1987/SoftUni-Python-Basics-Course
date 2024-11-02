start_num = int(input())
end_num = int(input())
magic_number = int(input())

combination_count = 0
found = False

for i in range (start_num, end_num + 1):
    for j in range(start_num, end_num + 1):
        combination_count += 1

        if i + j == magic_number:
            print (f"Combination N:{combination_count} ({i} + {j} = {magic_number})")
            found = True
            break

    if found:
        break

else:
    print(f"{combination_count} combinations - neither equals {magic_number}")
