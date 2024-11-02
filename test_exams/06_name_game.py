max_points = 0
winner = ""
result = None

while True:
    command = input()
    current_points = 0

    if command == "Stop":
        break

    for letter in command:
        number = int(input())

        if letter == chr(number):
            current_points += 10
        else:
            current_points += 2

    if current_points >= max_points:
        max_points = current_points
        winner = command

print(f"The winner is {winner} with {max_points} points!")

