name_of_movie = input()
days = int(input())
tickets = int(input())
price_of_ticket = float(input())
percent_for_cinema = int(input())

earnings = ((tickets * price_of_ticket) * days)

profit = earnings - (earnings * (percent_for_cinema / 100))

print(f"The profit from the movie {name_of_movie} is {profit:.2f} lv.")
