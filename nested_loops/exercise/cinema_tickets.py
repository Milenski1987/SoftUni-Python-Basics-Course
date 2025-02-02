student_tickets_count = standard_tickets_count = kids_tickets_count = 0
total_tickets = 0

while True:
    movie = input()

    if movie == "Finish":
        print(f"Total tickets: {total_tickets}")
        print(f"{student_tickets_count / total_tickets * 100:.2f}% student tickets.")
        print(f"{standard_tickets_count / total_tickets * 100:.2f}% standard tickets.")
        print(f"{kids_tickets_count / total_tickets * 100:.2f}% kids tickets.")
        break

    free_seats = int(input())
    tickets_sold = 0
    for _ in range(free_seats):
        command = input()

        if command == "End":
            print(f"{movie} - {(tickets_sold / free_seats * 100):.2f}% full.")
            break
        elif command == "student":
            student_tickets_count += 1
        elif command == "standard":
            standard_tickets_count += 1
        elif command == "kid":
            kids_tickets_count += 1

        tickets_sold += 1

        if tickets_sold == free_seats:
            print(f"{movie} - {(tickets_sold / free_seats * 100):.2f}% full.")
            break

    total_tickets += tickets_sold
