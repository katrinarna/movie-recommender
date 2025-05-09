#This file is our Website's server.
# It uses Flask to create a web application that recommends movies based on user input.
# It imports necessary libraries and modules, loads a dataset of movies, and sets up a Flask app.
# It defines a route for the home page and another for the recommendation feature.
# The recommendation feature uses a function from another module to get movie recommendations based on the title provided by the user.
from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
# This creates the app. static_folder is where our CSS lives.
app = Flask(__name__, template_folder="templates", static_folder="static")

# Load movies dataset
movies = pd.read_csv("movies.csv")

# Ensure title formatting is consistent (capitalize first letter of each word)
movies["title"] = movies["title"].str.strip().str.title()  # This ensures proper capitalization

# This converts each movie’s description into a number-based format (TF-IDF vectors).
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(movies["overview"].fillna(""))  # Handle missing overviews


# Compute similarity
# This calculates how similar each movie is to the others and maps each title to its row index.
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(movies.index, index=movies["title"]).drop_duplicates()

#This shows the homepage (the input box) when you visit the root URL.
@app.route("/")
def home():
    return render_template("index.html")

# This imports the function from recommend.py that does the actual recommendation.
from src.recommend import recommend_movies  

# This responds to searches by calling the recommend function and returning the results in JSON.
@app.route("/recommend")
def recommend():
    title = request.args.get("title", "").strip().title()  # Convert input to Title Case
    return jsonify(recommend_movies(title))  
# This runs the server when you type python app.py.
if __name__ == "__main__":
    app.run(debug=True)


