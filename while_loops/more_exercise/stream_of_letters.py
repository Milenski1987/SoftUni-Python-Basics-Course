c_count = o_count = n_count = 0
word = ""

while True:
    command = input()

    if command == "End":
        break

    if ord(command) < 65 or 90 < ord(command) < 97 or ord(command) > 122:
        continue

    if command == "c":
        if c_count == 0:
            c_count += 1
        else:
            word += command
    elif command == "o":
        if o_count == 0:
            o_count += 1
        else:
            word += command
    elif command == "n":
        if n_count == 0:
            n_count += 1
        else:
            word += command
    else:
        word += command

    if c_count == 1 and o_count == 1 and n_count == 1:
        print(f"{word}", end="")
        c_count = 0
        o_count = 0
        n_count = 0
        word = " "
