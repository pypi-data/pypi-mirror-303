from .film import Film
from .lists import UserList
from .user import User  

class Pyboxd:
    def __init__(self, user_name: str = None, film_name: str = None):
        self.user_name = user_name
        self.film_name = film_name
        self.user_list = None
        self.film = None
        self.user = None  

        if user_name:
            self.user_list = UserList(username=user_name)
            self.user = User(username=user_name)  
        if film_name:
            self.film = Film(film_name=film_name)

    def get_user_lists(self):
        """Fetches and returns the user's movie lists."""
        if self.user_list:
            return self.user_list.get_user_list()
        else:
            raise Exception("User name not provided")

    def get_user_details(self):
        """Fetches and returns user details."""
        if self.user:
            return self.user.get_user_details()  
        else:
            raise Exception("User name not provided")

    def get_user_reviews(self):
        """Fetches and returns user reviews."""
        if self.user:
            return self.user.get_user_reviews()  
        else:
            raise Exception("User name not provided")

    def get_film_details(self):
        """Fetches and returns details for the specified film."""
        if self.film:
            self.film.get_film_details()
            return self.film.filmDetails
        else:
            raise Exception("Film name not provided")

    def get_film_releases(self):
        """Fetches and returns film release details."""
        if self.film:
            self.film.get_film_releases()
            return self.film.filmReleases
        else:
            raise Exception("Film name not provided")

    def get_film_duration(self):
        """Fetches and returns film duration details."""
        if self.film:
            self.film.get_film_duration()
            return self.film.filmDuration
        else:
            raise Exception("Film name not provided")

    def get_film_similars(self):
        """Fetches and returns similar films."""
        if self.film:
            self.film.get_film_similars()
            return self.film.filmSimilars
        else:
            raise Exception("Film name not provided")
