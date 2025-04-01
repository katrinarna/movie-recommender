import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

if TMDB_API_KEY:
    print(f"✅ API Key Loaded: {TMDB_API_KEY}")
else:
    print("❌ API Key Not Loaded! Check your .env file.")
