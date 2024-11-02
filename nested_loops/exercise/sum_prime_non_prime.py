prime_numbers_sum = non_prime_numbers_sum = 0


while True:
    command = input()

    if command == "stop":
        break

    if int(command) < 0:
        print("Number is negative.")
        continue

    number = int(command)
    non_prime_found = False

    for num in range(2, number):
        if number % num == 0:
            non_prime_found = True

    if non_prime_found:
        non_prime_numbers_sum += number
    else:
        prime_numbers_sum += number


print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")




