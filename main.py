"""
Name:
Date Started:
Brief Project Description:
GitHub URL:
"""
# TODO: Create your main program in this file, using the MoviesApp class


"""
Name: Hu Zedong
Date started: 2025/8/7
GitHub URL:https://github.com/Asu-ka520/a2-movies-Asu-ka520-main
Kivy GUI program for managing movies - Assignment 2
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from moviecollection import MovieCollection
from movie import Movie

FILENAME = "movies.json"


class MoviesApp(App):
    """Main Kivy app for movie management"""

    def build(self):
        """Build the Kivy app interface"""
        self.title = "Movies To Watch 2.0"
        self.movie_collection = MovieCollection()

        # Load the app.kv file and build interface
        self.root = Builder.load_file('app.kv')

        # Load movies from file
        self.movie_collection.load_movies(FILENAME)

        # Setup the interface
        self.create_movie_buttons()
        self.update_status()

        return self.root

    def create_movie_buttons(self):
        """Create buttons for all movies"""
        # Clear existing buttons
        self.root.ids.movie_buttons.clear_widgets()

        # Add button for each movie
        for movie in self.movie_collection.movies:
            button = Button(
                text=f"{movie.title} ({movie.year})",
                size_hint_y=None,
                height=40
            )

            # Set button color based on watched status
            if movie.is_watched:
                button.background_color = (0.2, 0.8, 0.2, 1)  # Green for watched
            else:
                button.background_color = (0.8, 0.2, 0.2, 1)  # Red for unwatched

            # Bind button press to toggle watched status
            button.bind(on_press=lambda x, m=movie: self.toggle_watched(m))

            self.root.ids.movie_buttons.add_widget(button)

    def toggle_watched(self, movie):
        """Toggle the watched status of a movie"""
        if movie.is_watched:
            movie.mark_unwatched()
        else:
            movie.mark_watched()

        # Update interface
        self.create_movie_buttons()
        self.update_status()

        # Save changes
        self.movie_collection.save_movies(FILENAME)

    def sort_movies(self):
        """Sort movies based on spinner selection"""
        sort_choice = self.root.ids.sort_spinner.text

        if sort_choice == "Title":
            self.movie_collection.sort_by_title()
        elif sort_choice == "Year":
            self.movie_collection.sort_by_year()
        elif sort_choice == "Category":
            self.movie_collection.sort_by_category()

        # Update movie buttons display
        self.create_movie_buttons()

    def add_movie(self):
        """Add a new movie from input fields"""
        title = self.root.ids.title_input.text.strip()
        year_text = self.root.ids.year_input.text.strip()
        category = self.root.ids.category_input.text.strip()

        # Validate inputs
        if not title:
            self.update_status("Title cannot be blank")
            return

        if not category:
            self.update_status("Category cannot be blank")
            return

        try:
            year = int(year_text)
            if year < 0:
                self.update_status("Year must be >= 0")
                return
        except ValueError:
            self.update_status("Please enter a valid year")
            return

        # Add the movie
        new_movie = Movie(title, category, year, False)
        self.movie_collection.add_movie(new_movie)

        # Update interface
        self.create_movie_buttons()
        self.clear_fields()
        self.update_status(f"Added {title}")

        # Save changes
        self.movie_collection.save_movies(FILENAME)

    def clear_fields(self):
        """Clear all input fields"""
        self.root.ids.title_input.text = ""
        self.root.ids.year_input.text = ""
        self.root.ids.category_input.text = ""

    def update_status(self, message=""):
        """Update the status label"""
        if message:
            self.root.ids.status_label.text = message
        else:
            unwatched = self.movie_collection.get_number_of_unwatched_movies()
            total = self.movie_collection.get_number_of_movies()
            self.root.ids.status_label.text = f"Movies to watch: {unwatched}. Total movies: {total}"


if __name__ == "__main__":
    MoviesApp().run()
