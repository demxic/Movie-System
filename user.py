from movie import Movie


class User(object):
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre, watched):
        self.movies.append(Movie(name, genre, True))

    def delete_movie(self, name):
        return list(filter(lambda movie: movie.name != name, self.movies))

    def get_movie(self, name):
        fil = filter(lambda movie : movie.name == name, self.movies)
        return list(fil)[0]

    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + '\n')
            for movie in self.movies:
                f.write('{},{},{}'.format(movie.name, movie.genre, movie.watched) + '\n')

    @classmethod
    def load_from_file(cls, filename):
        with open('{}.txt'.format(filename), 'r') as f:
            username = f.readline()
            movies = []
            for line in f.readlines():
                name, genre, watched = line.split(',')
                movies.append(Movie(name, genre, watched == 'True'))
        user = cls(username)
        user.movies = movies
        return user

    def json(self):
        return {'name': self.name,
                'movies': [movie.json() for movie in self.movies]
                }

    @classmethod
    def from_json(cls, json_data):
        user_name = json_data['name']
        movies = [Movie.from_json(movie_data) for movie_data in json_data['movies']]
        user = cls(user_name)
        user.movies = movies
        return user

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))
