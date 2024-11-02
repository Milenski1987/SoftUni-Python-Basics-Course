student_tickets_count = standard_tickets_count = kid_tickets_count = 0
total_tickets = 0

while True:
    movie = input()

    if movie == "Finish":
        print(f"Total tickets: {total_tickets}")
        print(f"{(student_tickets_count / total_tickets * 100):.2f}% student tickets.")
        print(f"{(standard_tickets_count / total_tickets * 100):.2f}% standard tickets.")
        print(f"{(kid_tickets_count / total_tickets* 100):.2f}% kids tickets.")
        break

    people_counter = 0
    free_seats = int(input())

    for seat in range(free_seats):
        type_of_ticket = input()

        if type_of_ticket == "End":
            break
        elif type_of_ticket == "student":
            student_tickets_count += 1
            total_tickets += 1
        elif type_of_ticket == "standard":
            standard_tickets_count += 1
            total_tickets += 1
        elif type_of_ticket == "kid":
            kid_tickets_count += 1
            total_tickets += 1

        people_counter += 1

    print(f"{movie} - {((people_counter / free_seats) * 100):.2f}% full.")

