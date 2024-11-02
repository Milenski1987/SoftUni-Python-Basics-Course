cake_length = int(input())
cake_width = int(input())

total_cake_pieces = cake_width * cake_length
pieces_taken = 0

while total_cake_pieces > pieces_taken:
    command = input()

    if command == "STOP":
        print(f"{total_cake_pieces - pieces_taken} pieces are left.")
        break

    cake_pieces = int(command)
    pieces_taken += cake_pieces

else:
    print(f"No more cake left! You need {pieces_taken - total_cake_pieces} pieces more.")
