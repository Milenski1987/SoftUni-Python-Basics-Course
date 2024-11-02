control_value = int(input())

passwords_found_counter = 0

found = False
password = None

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):

                if (a * b) + (c * d) == control_value and a < b and c > d:
                    passwords_found_counter += 1
                    print(f"{a}{b}{c}{d}", end=" ")

                    if passwords_found_counter == 4:
                        password = f"Password: {a}{b}{c}{d}"
                        found = True

print()

if found:
    print(password)
else:
    print("No!")
