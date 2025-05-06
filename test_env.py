# Checking our API Key
# Tells you if your .env file is working correctly and the API key is loaded.
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

if TMDB_API_KEY:
    print(f"✅ API Key Loaded: {TMDB_API_KEY}")
else:
    print("❌ API Key Not Loaded! Check your .env file.")
