max_score = 0
most_powerful_word = ""

while True:
    command = input()
    current_score = 0

    if command == "End of words":
        break

    for letter in command:
        current_score += ord(letter)

    if command[0] in "aeiouy" or command[0] in "AEIOUY":
        current_score = current_score * len(command)
    else:
        current_score = current_score // len(command)

    if current_score > max_score:
        max_score = current_score
        most_powerful_word = command

print(f"The most powerful word is {most_powerful_word} - {max_score}")
