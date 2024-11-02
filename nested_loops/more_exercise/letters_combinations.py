start_of_interval = input()
end_of_interval = input()
letter_to_be_miss = input()

printed_count = 0

for letter1 in range(ord(start_of_interval), ord(end_of_interval) + 1):
    if chr(letter1) != letter_to_be_miss:
        for letter2 in range(ord(start_of_interval), ord(end_of_interval) + 1):
            if chr(letter2) != letter_to_be_miss:
                for letter3 in range(ord(start_of_interval), ord(end_of_interval) + 1):
                    if chr(letter3) != letter_to_be_miss:
                        printed_count += 1
                        print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}", end=" ")

print(printed_count)