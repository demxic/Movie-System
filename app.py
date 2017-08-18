import json

from user import User


def menu():
    user_name = input("What is your name? : ")
    try:
        with open("{}.txt".format(user_name), 'r') as f:
            user = User.from_json(json.load(f))
            print("Welcome {}".format(user.name))
    except FileNotFoundError:
        user = User(user_name)
    option = 'p'
    while option != 'q':
        option = input("What is your option? \n"
                       "a to add a movie\n"
                       "l to see a list of movies\n"
                       "w to set a movie as watched\n"
                       "d to delete a movie by name\n"
                       "m to see a list of watched movies\n"
                       "q to save and quit\n")
        if option == 'a':
            movie_name = input("What is the movie's name? :")
            genre = input("What is its genre? :")
            watched = input("Have you watched it before? (True or False): ")
            user.add_movie(movie_name, genre, watched)
        elif option == 'l':
            print(user.movies)
        elif option == 'w':
            movie_name = input("Enter movie's name : ")
            movie = user.get_movie(movie_name)
            movie.watched = True
        elif option == 'd':
            movie_name = input("Enter movie's name : ")
            print(user.delete_movie(movie_name))
        elif option == 'm':
            print(user.watched_movies())
        elif option == 'q':
            json_data = user.json()
            with open('{}.txt'.format(user.name), 'w') as f:
                json.dump(json_data, f)


menu()
