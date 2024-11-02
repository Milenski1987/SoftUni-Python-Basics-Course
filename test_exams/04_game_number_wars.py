first_player_name = input()
second_player_name = input()

first_player_score = second_player_score = 0
winner = ""
winner_score = 0

while True:
    command = input()

    if command == "End of game":
        print(f"{first_player_name} has {first_player_score} points")
        print(f"{second_player_name} has {second_player_score} points")
        break

    first_player_card = int(command)
    second_player_card = int(input())

    if first_player_card > second_player_card:
        first_player_score += first_player_card - second_player_card
    elif second_player_card > first_player_card:
        second_player_score += second_player_card - first_player_card
    else:
        first_player_additional_card = int(input())
        second_player_additional_card = int(input())
        if first_player_additional_card > second_player_additional_card:
            winner = first_player_name
            winner_score = first_player_score
        elif second_player_additional_card > first_player_additional_card:
            winner = second_player_name
            winner_score = second_player_score
        print("Number wars!")
        print(f"{winner} is winner with {winner_score} points")
        break
        