from movie import Movie
from user import User

my_movie = Movie('The Matrix', 'Sci-Fi', True)
print(my_movie.name)
user = User('Xico')
print(user)
user.movies.append(my_movie)
print(user.watched_movies())