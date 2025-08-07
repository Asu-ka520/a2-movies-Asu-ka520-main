"""..."""


# TODO: Create your Movie class in this file

"""
Movie class for storing movie information
"""


class Movie:
    """Represent a Movie with title, category, year and watched status"""

    def __init__(self, title="", category="", year=0, is_watched=False):
        """Initialize a Movie instance

        Args:
            title (str): The movie title
            category (str): The movie category/genre
            year (int): The release year
            is_watched (bool): Whether the movie has been watched
        """
        self.title = title
        self.category = category
        self.year = year
        self.is_watched = is_watched

    def __str__(self):
        """Return a string representation of the movie"""
        watched_status = "watched" if self.is_watched else "unwatched"
        return f"{self.title} ({self.category} from {self.year}) - {watched_status}"

    def mark_watched(self):
        """Mark the movie as watched"""
        self.is_watched = True

    def mark_unwatched(self):
        """Mark the movie as unwatched"""
        self.is_watched = False

    def is_valid(self):
        """Check if the movie has valid data

        Returns:
            bool: True if all fields are valid, False otherwise
        """
        return (self.title != "" and
                self.category != "" and
                self.year > 0)
