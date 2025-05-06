# This file contains the logic that figures out which movies to recommend.

# It uses the cosine similarity of movie descriptions and genre matching to find similar movies.
# It also fetches additional movie details from the TMDb API.
# This file is our recommendation engine.


# Importing data tools, similarity tools, and .env handling for API keys.
import pandas as pd
import requests
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Loading the movie data and ensures overview is filled. Parses genre IDs from strings into lists.
df = pd.read_csv("movies.csv")
df["overview"] = df["overview"].fillna("")
df["genre_ids"] = df["genre_ids"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])

# Converts overviews to vectors and computes similarity. Creates a mapping of title to index.
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["overview"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

TMDB_API_KEY = os.getenv("TMDB_API_KEY")  # Fetch the API key

# Debugging Print
print(f"✅ Loaded API Key: {TMDB_API_KEY}")  # Check if key is loaded

# This function uses the TMDb API to find poster, genres, runtime, etc. for a movie title.
def get_movie_details(title):
    print(f"\n🔥 FETCHING DETAILS FOR: {title}")

    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"
    response = requests.get(url).json()
    results = response.get("results", [])

    if not results:
        return {
            "poster_url": "https://via.placeholder.com/150",
            "overview": "No description available.",
            "vote_average": "N/A",
            "release_date": "N/A",
            "genres": [],
            "runtime": "N/A"
        }

    movie = results[0]
    movie_id = movie["id"]

    # Fetch full movie details by ID
    detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    detail_response = requests.get(detail_url).json()

    poster_url = f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get("poster_path") else "https://via.placeholder.com/150"

    # Extract genres nicely
    genres = [g["name"] for g in detail_response.get("genres", [])]

    return {
        "poster_url": poster_url,
        "overview": detail_response.get("overview", "No description available."),
        "vote_average": detail_response.get("vote_average", "N/A"),
        "release_date": detail_response.get("release_date", "N/A"),
        "genres": genres,
        "runtime": detail_response.get("runtime", "N/A")
    }

# Main function that:
# Finds the input movie.
# Calculates similarity to all others.
# Boosts scores based on genre match and rating.
# Returns top 5 movies with full metadata from TMDb.

def recommend_movies(title, n=5):
    if title not in indices:
        return {"error": f"❌ Movie '{title}' not found in dataset!"}

    idx = indices[title]
    target_genres = df.loc[idx]["genre_ids"]

    sim_scores = list(enumerate(cosine_sim[idx]))

    # Add genre match boost
    scored = []
    for i, score in sim_scores:
        movie_genres = df.iloc[i]["genre_ids"]
        genre_overlap = len(set(target_genres).intersection(set(movie_genres)))
        vote_avg = df.iloc[i]["vote_average"]
        final_score = score + (0.05 * genre_overlap) + (0.01 * vote_avg)
        scored.append((i, final_score))

    # Sort and select top matches
    scored = sorted(scored, key=lambda x: x[1], reverse=True)
    movie_indices = [i for i, _ in scored[1:n+1]]
    recommendations = []
    for movie_title in df["title"].iloc[movie_indices].tolist():
        movie_data = get_movie_details(movie_title)  # Call the new function
        recommendations.append({
        "title": movie_title,
        "poster": movie_data["poster_url"],
        "overview": movie_data["overview"],
        "vote_average": movie_data["vote_average"],
        "release_date": movie_data["release_date"],
        "genres": movie_data["genres"],
        "runtime": movie_data["runtime"]
    })
    return {"recommendations": recommendations}


# Flask Route
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    title = request.args.get('title', '')
    results = recommend_movies(title)
    print(results)  # Print response in the Flask terminal to debug
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
