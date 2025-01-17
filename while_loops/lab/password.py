username = input()
password = input()

while True:
    data = input()

    if data != password:
        continue

    print(f"Welcome {username}!")
    break
