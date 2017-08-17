from movie import Movie


class User(object):
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        self.append(Movie(name, genre, True))

    def delete_movie(self, name):
        filter(lambda movie: movie.name != name, self.movies)

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))
