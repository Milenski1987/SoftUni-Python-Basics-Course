book = input()

checked_books = 0

while True:
    command = input()

    if command == "No More Books":
        print(f"The book you search is not here!\nYou checked {checked_books} books.")
        break

    if command == book:
        print(f"You checked {checked_books} books and found it.")
        break

    checked_books += 1
