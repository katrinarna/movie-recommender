# This script is only run once to build the movies.csv.
# It fetches movie data from TMDb API and saves it to a CSV file.
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import time

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

# Function to fetch movies from TMDb
def get_movies(page=1):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
    response = requests.get(url)
    data = response.json()

    movies = []
    for movie in data.get("results", []):
        movies.append({
            "title": movie["title"],
            "release_date": movie.get("release_date", "N/A"),
            "vote_average": movie.get("vote_average", 0),
            "vote_count": movie.get("vote_count", 0),
            "overview": movie.get("overview", "No description available"),
            "genre_ids": movie.get("genre_ids", [])
        })

    return movies

# Calls the TMDb API to get a page of popular movies.
# Collects movies from 100 pages (~2000 movies) and avoids API rate limits.
all_movies = []
TOTAL_PAGES = 100  # We can adjust this number to fetch more.
for page in range(1, TOTAL_PAGES + 1):
    print(f"📥 Fetching page {page}...")
    all_movies.extend(get_movies(page))
    time.sleep(0.5)  # Prevent rate limiting

# Convert to DataFrame and save
df = pd.DataFrame(all_movies)
df.to_csv("movies.csv", index=False)
print(f"✅ {len(df)} movies saved to movies.csv!")


