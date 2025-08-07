"""..."""
# TODO: Copy your first assignment to this file, then update it to use your classes


"""
Name: Hu Zedong
Date started: 2025/8/7
GitHub URL: https://github.com/cp1404-students/a2-movies-Asu-ka520
Console program for managing movies using Movie and MovieCollection classes
"""

from movie import Movie
from moviecollection import MovieCollection

FILENAME = "movies.json"
CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]


def main():
    """Main function to manage the must-see movies program."""
    print("Must-See Movies - by Hu Zedong")

    movie_collection = MovieCollection()
    movie_collection.load_movies(FILENAME)
    print(f"{movie_collection.get_number_of_movies()} movies loaded from {FILENAME}")

    while True:
        print_menu()
        choice = input(">>> ").strip().lower()
        if choice == "d":
            display_movies(movie_collection)
        elif choice == "a":
            add_movie(movie_collection)
        elif choice == "w":
            watch_movie(movie_collection)
        elif choice == "q":
            movie_collection.save_movies(FILENAME)
            print(f"{movie_collection.get_number_of_movies()} movies saved to {FILENAME}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def print_menu():
    """Print the menu options."""
    print("Menu:")
    print("D - Display movies")
    print("A - Add new movie")
    print("W - Watch a movie")
    print("Q - Quit")


def display_movies(movie_collection):
    """Display the list of movies in required format, sorted by year then title."""
    if movie_collection.get_number_of_movies() == 0:
        print("No movies to display")
        return

    # Sort movies for display (year then title)
    movie_collection.movies.sort(key=lambda m: (m.year, m.title.lower()))

    watched_count = 0
    unwatched_count = 0

    # Find max widths for formatting
    max_title = max([len(movie.title) for movie in movie_collection.movies])
    max_cat = max([len(movie.category) for movie in movie_collection.movies])

    for i, movie in enumerate(movie_collection.movies, 1):
        marker = "*" if not movie.is_watched else " "
        print(f"{i:2}. {marker} {movie.title.ljust(max_title)}  -  {str(movie.year).rjust(4)} ({movie.category})")
        if movie.is_watched:
            watched_count += 1
        else:
            unwatched_count += 1

    print(f"{watched_count} movies watched. {unwatched_count} movies still to watch.")


def add_movie(movie_collection):
    """Prompt for movie details, check validity, and add a new unwatched movie."""
    title = get_non_empty_input("Title: ")
    year = get_positive_int("Year: ")
    print(f"Categories available: {', '.join(CATEGORIES)}")
    category = input_with_category()

    new_movie = Movie(title, category, year, False)
    movie_collection.add_movie(new_movie)
    print(f"{title} ({category} from {year}) added to movie list")


def watch_movie(movie_collection):
    """Prompt user to mark an unwatched movie as watched, with error checking."""
    unwatched_movies = [movie for movie in movie_collection.movies if not movie.is_watched]
    if not unwatched_movies:
        print("No more movies to watch!")
        return

    print("Enter the movie number to mark watched.")

    # Sort movies for consistent display
    sorted_movies = sorted(movie_collection.movies, key=lambda m: (m.year, m.title.lower()))

    while True:
        try:
            user_input = input(">>> ")
            movie_number = int(user_input)
            if movie_number < 1:
                print("Number must be >= 1")
                continue
            if movie_number > len(sorted_movies):
                print("Invalid movie number.")
                continue

            selected_movie = sorted_movies[movie_number - 1]
            if selected_movie.is_watched:
                print(f"You have already watched {selected_movie.title}.")
            else:
                selected_movie.mark_watched()
                print(f"{selected_movie.title} ({selected_movie.year}) watched.")
            break
        except ValueError:
            print("Invalid input; enter a valid number")


def get_non_empty_input(prompt):
    """Prompt until non-blank input is entered."""
    while True:
        result = input(prompt)
        if result.strip():
            return result.strip()
        else:
            print("Input can not be blank")


def get_positive_int(prompt):
    """Prompt until a valid positive integer is entered."""
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Number must be >= 1")
            else:
                return value
        except ValueError:
            print("Invalid input; enter a valid number")


def input_with_category():
    """Ask the user for a valid category, default to Other if not valid."""
    while True:
        category = input("Category: ").strip()
        if not category:
            print("Input can not be blank")
            continue
        # Case-insensitive matching
        matches = [cat for cat in CATEGORIES if cat.lower() == category.lower()]
        if matches:
            return matches[0]
        else:
            print("Invalid category; using Other")
            return "Other"


if __name__ == '__main__':
    main()
