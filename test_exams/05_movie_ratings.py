number_of_chosen_movies = int(input())
highest_rating = lowest_rating = average_rating = 0
highest_rate_movie = lowest_rate_movie = ""
total_rating = 0

for movie in range(1, number_of_chosen_movies + 1):
    movie_name = input()
    movie_rating = float(input())

    total_rating += movie_rating

    if movie == 1:
        highest_rate_movie = movie_name
        highest_rating = movie_rating
        lowest_rate_movie = movie_name
        lowest_rating = movie_rating

    if movie_rating > highest_rating:
        highest_rate_movie = movie_name
        highest_rating = movie_rating
    elif movie_rating < lowest_rating:
        lowest_rate_movie = movie_name
        lowest_rating = movie_rating


print(f"{highest_rate_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rate_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {(total_rating / number_of_chosen_movies):.1f}")