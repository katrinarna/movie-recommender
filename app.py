from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__, static_folder="static")


# Load movies dataset
movies = pd.read_csv("movies.csv")

# Ensure title formatting is consistent (capitalize first letter of each word)
movies["title"] = movies["title"].str.strip().str.title()  # This ensures proper capitalization

# Prepare TF-IDF Vectorizer for movie overviews (descriptions)
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(movies["overview"].fillna(""))  # Handle missing overviews

# Compute similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Movie title to index mapping
indices = pd.Series(movies.index, index=movies["title"]).drop_duplicates()

@app.route("/")
def home():
    return render_template("index.html")

from recommend import recommend_movies  # ✅ Import the correct function

@app.route("/recommend")
def recommend():
    title = request.args.get("title", "").strip().title()  # Convert input to Title Case
    return jsonify(recommend_movies(title))  # ✅ Use the correct function from recommend.py

if __name__ == "__main__":
    app.run(debug=True)


