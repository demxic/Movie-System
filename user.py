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

    def save_to_file(self):
        with open ("{}.txt".format(self.name), 'w') as f:
            f.write(self.name+'\n')
            for movie in self.movies:
                f.write('{},{},{}'.format(movie.name, movie.genre, movie.watched)+'\n')

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))
