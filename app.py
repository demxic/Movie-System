from movie import Movie
from user import User

my_movie = Movie('The Matrix', 'Sci-Fi', True)

user = User('Xico')
user.add_movie('The Matrix', 'Sci-Fi', False)
user.add_movie('No sé', 'comedia', False)
user.save_to_file()
