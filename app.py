from movie import Movie
from user import User

my_movie = Movie('The Matrix', 'Sci-Fi', True)

user = User.load_from_file('Xico')
print(user.movies)
