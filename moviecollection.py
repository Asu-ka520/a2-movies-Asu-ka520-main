"""..."""


# TODO: Create your MovieCollection class in this file


"""
MovieCollection class for managing a collection of movies
"""

import json
from movie import Movie


class MovieCollection:
    """Manage a collection of Movie objects"""

    def __init__(self):
        """Initialize an empty movie collection"""
        self.movies = []

    def load_movies(self, filename):
        """Load movies from a JSON file

        Args:
            filename (str): Path to the JSON file containing movie data
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.movies = []
                for movie_data in data.values():
                    movie = Movie(movie_data['title'],
                                  movie_data['category'],
                                  movie_data['year'],
                                  movie_data['is_watched'])
                    self.movies.append(movie)
        except FileNotFoundError:
            print(f"Error: File {filename} not found")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in file {filename}")

    def save_movies(self, filename):
        """Save movies to a JSON file

        Args:
            filename (str): Path to save the JSON file
        """
        data = {}
        for i, movie in enumerate(self.movies):
            data[str(i)] = {
                'title': movie.title,
                'category': movie.category,
                'year': movie.year,
                'is_watched': movie.is_watched
            }

        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=2)
        except IOError:
            print(f"Error: Could not write to file {filename}")

    def add_movie(self, movie):
        """Add a movie to the collection

        Args:
            movie (Movie): The movie to add
        """
        self.movies.append(movie)

    def get_number_of_movies(self):
        """Get the total number of movies

        Returns:
            int: Total number of movies
        """
        return len(self.movies)

    def get_number_of_unwatched_movies(self):
        """Get the number of unwatched movies

        Returns:
            int: Number of unwatched movies
        """
        count = 0
        for movie in self.movies:
            if not movie.is_watched:
                count += 1
        return count

    def sort_by_title(self):
        """Sort movies by title alphabetically"""
        self.movies.sort(key=lambda x: x.title)

    def sort_by_year(self):
        """Sort movies by year (newest first)"""
        self.movies.sort(key=lambda x: x.year, reverse=True)

    def sort_by_category(self):
        """Sort movies by category alphabetically"""
        self.movies.sort(key=lambda x: x.category)

    def __str__(self):
        """Return string representation of the collection"""
        if not self.movies:
            return "No movies in collection"

        result = []
        for i, movie in enumerate(self.movies):
            result.append(f"{i}. {movie}")
        return "\n".join(result)

