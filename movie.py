class Movie(object):
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def json(self):
        return {'name': self.name,
                'genre': self.genre,
                'watched': self.watched}

    @classmethod
    def from_json(cls, movie_data):
        movie = cls(movie_data['name'], movie_data['genre'], movie_data['watched'])
        return movie

    def __repr__(self):
        return "<Movie {}>".format(self.name)
