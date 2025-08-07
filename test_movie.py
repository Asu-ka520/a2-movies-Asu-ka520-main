"""(Incomplete) Tests for Movie class."""

"""
Test file for Movie class
"""

from movie import Movie


def run_tests():
    """Run tests for Movie class"""
    print("Testing Movie class...")

    # Test empty movie
    print("\nTest 1: Empty movie")
    empty_movie = Movie()
    print(f"Empty movie: {empty_movie}")
    print(f"Is valid: {empty_movie.is_valid()}")
    assert empty_movie.title == ""
    assert empty_movie.category == ""
    assert empty_movie.year == 0
    assert empty_movie.is_watched == False

    # Test movie with data
    print("\nTest 2: Movie with data")
    movie = Movie("Thor: Ragnarok", "Comedy", 2017, True)
    print(f"Movie: {movie}")
    print(f"Is valid: {movie.is_valid()}")
    assert movie.title == "Thor: Ragnarok"
    assert movie.category == "Comedy"
    assert movie.year == 2017
    assert movie.is_watched == True

    # Test mark watched/unwatched
    print("\nTest 3: Mark watched/unwatched")
    movie2 = Movie("Test Movie", "Action", 2020, False)
    print(f"Before marking watched: {movie2}")
    movie2.mark_watched()
    print(f"After marking watched: {movie2}")
    assert movie2.is_watched == True

    movie2.mark_unwatched()
    print(f"After marking unwatched: {movie2}")
    assert movie2.is_watched == False

    # Test invalid movie
    print("\nTest 4: Invalid movie")
    invalid_movie = Movie("", "Action", 0, False)
    print(f"Invalid movie is valid: {invalid_movie.is_valid()}")
    assert invalid_movie.is_valid() == False

    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()

