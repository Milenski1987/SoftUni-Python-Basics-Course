movie_counter = 0
best_movie = ""
best_score = 0

while True:
    current_score = 0
    command = input()

    if command == "STOP":
        break

    for char in command:
        if 65 <= ord(char) <= 90:
            current_score += ord(char) - len(command)
        elif 97 <= ord(char) <= 122:
            current_score += ord(char) - (2 * len(command))
        else:
            current_score += ord(char)

    if current_score > best_score:
        best_movie = command
        best_score = current_score

    movie_counter += 1

    if movie_counter == 7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {best_movie} with {best_score} ASCII sum.")

