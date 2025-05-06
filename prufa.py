# This script is our mini lab for checking data.
import pandas as pd

df = pd.read_csv("movies.csv")
#Shows the first few rows and some details about the data.
print(df.head())
print(df.info()) 

# Cleans up missing or duplicate data.
df.fillna({"release_date": "Unknown", "overview": "No description available"}, inplace=True)
df.drop_duplicates(subset="title", keep="first", inplace=True)

# Print some sample movie titles to check formatting
print(movies["title"].head(10))  

# Check if 'Gone Girl' exists in any format
print("Gone Girl" in movies["title"].values)
