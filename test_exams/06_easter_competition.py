number_of_coz = int(input())
max_points = 0
chef_with_max_points = ""

for coz in range(number_of_coz):
    name_of_chef = input()
    chef_points = 0

    while True:
        command = input()

        if command == "Stop":
            print(f"{name_of_chef} has {chef_points} points.")
            if chef_points > max_points:
                max_points = chef_points
                chef_with_max_points = name_of_chef
                print(f"{name_of_chef} is the new number 1!")
            break

        points = int(command)
        chef_points += points

print(f"{chef_with_max_points} won competition with {max_points} points!")

