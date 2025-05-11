import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# This test file is for testing the recommend_movies function from the recommend module.
# It checks if the function returns the expected recommendations for a valid movie title,
# handles invalid movie titles gracefully, and checks for empty title inputs.


import pytest
from recommend import recommend_movies

def test_valid_movie_returns_recommendations():
    response = recommend_movies("Inception")
    assert "recommendations" in response
    assert len(response["recommendations"]) == 5

def test_invalid_movie_returns_error():
    response = recommend_movies("SomeUnknownMovieXYZ")
    assert "error" in response
    assert "not found" in response["error"]

def test_empty_title_returns_error():
    response = recommend_movies("")
    assert "error" in response
