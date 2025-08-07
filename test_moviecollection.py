"""(Incomplete) Tests for MovieCollection class."""
"""
Test file for MovieCollection class
"""

from moviecollection import MovieCollection
from movie import Movie

def run_tests():
    """Run tests for MovieCollection class"""
    print("Testing MovieCollection class...")

    # Test empty collection
    print("\nTest 1: Empty collection")
    collection = MovieCollection()
    print(f"Number of movies: {collection.get_number_of_movies()}")
    print(f"Number of unwatched: {collection.get_number_of_unwatched_movies()}")
    assert collection.get_number_of_movies() == 0
    assert collection.get_number_of_unwatched_movies() == 0

    # Test adding movies
    print("\nTest 2: Adding movies")
    movie1 = Movie("Test Movie 1", "Action", 2020, False)
    movie2 = Movie("Test Movie 2", "Comedy", 2019, True)
    collection.add_movie(movie1)
    collection.add_movie(movie2)
    print(f"Number of movies: {collection.get_number_of_movies()}")
    print(f"Number of unwatched: {collection.get_number_of_unwatched_movies()}")
    assert collection.get_number_of_movies() == 2
    assert collection.get_number_of_unwatched_movies() == 1

    # Test loading from file
    print("\nTest 3: Loading from file")
    collection2 = MovieCollection()
    collection2.load_movies("movies_backup.json")
    print(f"Loaded movies: {collection2.get_number_of_movies()}")
    print(f"Unwatched movies: {collection2.get_number_of_unwatched_movies()}")

    # Test sorting
    print("\nTest 4: Sorting by year")
    collection2.sort_by_year()
    print("Movies sorted by year:")
    for movie in collection2.movies[:3]:  # Just show first 3
        print(f"  {movie}")

    print("\nTest 5: Sorting by title")
    collection2.sort_by_title()
    print("Movies sorted by title:")
    for movie in collection2.movies[:3]:  # Just show first 3
        print(f"  {movie}")

    # Test saving
    print("\nTest 6: Saving to file")
    collection2.save_movies("test_output.json")
    print("Saved to test_output.json")

    print("\nAll tests completed!")

if __name__ == "__main__":
    run_tests()

