# 🎬 Movie Recommender System

This project is a **content-based movie recommendation engine** built using Python, Flask, and TMDb API. It recommends movies based on **cosine similarity** of movie descriptions and **genre overlap**, enhancing results with **real-time movie metadata** such as posters, runtime, and rating via the TMDb API.

---

## 📁 Project Structure

movie-recommender/
├── static/ # Static files (CSS, JS, images if any)
├── templates/ # HTML templates for Flask (if used)
├── .env # Environment variables (contains TMDb API key)
├── .gitignore # Git ignore rules
├── app.py # Flask app entry point
├── fetch_movies.py # (Optional) Script for fetching or preprocessing movies
├── movies.csv # Dataset containing movie metadata
├── prufa.py # (Optional) Test or development script
├── README.md # Project documentation
├── recommend.py # Core recommendation logic (similarity, TMDb API integration)
├── requirements.txt # Project dependencies
├── environment.yml # Conda environment file
└── test_env.py # Script to test environment or API key loading


---

## 🚀 Features

- Recommends similar movies based on description and genre
- Retrieves posters, genres, vote average, and runtime from TMDb
- Simple API access via Flask
- Easily extendable for web or mobile integration

---

## ⚙️ Installation


## ⚙️ Installation (with venv)

1. Clone the repository:

git clone https://github.com/katrinarna/movie-recommender
cd movie-recommender

2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies:
pip install -r requirements.txt

4. Create a .env file in the root directory and add your API key

TMDB_API_KEY=your_api_key_here

5. Run the application:

python app.py


---

## 👥 Contributing

1. Fork the repo and create your branch: git checkout -b feature-name

2. Commit your changes and push:
git commit -m "Add feature"
git push origin feature-name

3. Open a Pull Request

---

## 📚 Citation

If you use this project in your research or development, consider citing:
Movie Recommender Engine (2025). GitHub Repository. https://github.com/katrinarna/movie-recommender 
